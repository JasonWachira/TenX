from flask import Flask, jsonify, request
from flask_cors import CORS
from models import db, County, Candidate, Donation, Expense, Party, seed_data
from sqlalchemy import func, distinct

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campaign_finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)
db.init_app(app)

with app.app_context():
    seed_data()


@app.route("/api/v1/overview")
def overview():
    total_raised = db.session.query(func.sum(Candidate.total_raised)).scalar() or 0
    total_spent = db.session.query(func.sum(Candidate.total_spent)).scalar() or 0

    unique_donors = (db.session.query(func.count(distinct(Donation.donor_name)))
                     .filter(Donation.donor_name != "Anonymous")
                     .scalar() or 0)

    # Flagged candidates (if total_spending > legal_limit)
    flagged_count = Candidate.query.filter(
        Candidate.total_spent > Candidate.legal_spending_limit
    ).count()

    # Used as the denominator in calculating percentage of the total donations
    global_total = db.session.query(func.sum(Donation.amount)).scalar() or 1

    # Group sums according to donor_type. will return (donorType, amount)
    source_query = db.session.query(
        Donation.donor_type,
        func.sum(Donation.amount)
    ).group_by(Donation.donor_type).all()

    print(source_query)
    source_breakdown = []
    for donor_type, amount in source_query:
        percentage = round((amount / global_total) * 100, 1)
        source_breakdown.append({
            "label": donor_type or "Unknown",
            "value": amount,
            "percentage": percentage
        })

    bar_data = [
        {
            "name": c.full_name,
            "amount": c.total_raised,
            "flagged": (c.total_raised > c.legal_spending_limit)
        }
        for c in Candidate.query.limit(5).all()
    ]

    return jsonify({
        "kpi": {
            "total_raised": total_raised,
            "total_spent": total_spent,
            "flagged": flagged_count,
            "donors_count": unique_donors
        },
        "bar_data": bar_data,
        "source_breakdown": source_breakdown
    })


@app.route('/api/v1/candidates/<int:candidate_id>/analysis')
def get_candidate_analysis(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)

    spending_trends = db.session.query(
        func.date(Expense.date_incurred).label('date'),
        func.sum(Expense.amount).label('amount')
    ).filter(Expense.candidate_id == candidate_id) \
        .group_by(func.date(Expense.date_incurred)) \
        .order_by('date').all()

    top_donors = db.session.query(
        Donation.donor_name,
        func.sum(Donation.amount).label('total')
    ).filter(Donation.candidate_id == candidate_id) \
        .group_by(Donation.donor_name) \
        .order_by(db.desc('total')).all()

    comparison = {
        "received": candidate.total_raised,
        "spent": candidate.total_spent,
        "balance": candidate.total_raised - candidate.total_spent
    }

    flags = []
    if top_donors and (top_donors[0][1] / (candidate.total_raised or 1)) > 0.5:
        flags.append({
            "type": "High Donor Concentration",
            "detail": f"Top donor ({top_donors[0][0]}) accounts for {round((top_donors[0][1] / candidate.total_raised) * 100)}% of funds.",
            "severity": "Red"
        })

    return jsonify({
        "name": candidate.full_name,
        "line_chart": [{"date": r.date, "amount": r.amount} for r in spending_trends],
        "donor_pie": [{"name": r.donor_name, "value": r.total} for r in top_donors],
        "comparison_bar": comparison,
        "risk_flags": flags
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
