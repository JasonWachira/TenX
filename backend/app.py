from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, distinct

from models.db import engine, Base
from models.models import Candidate, Donation, Expense
from dependencies import get_db
from seeds import seed_data

app = FastAPI(title="Campaign Finance Transparency API")

Base.metadata.create_all(bind=engine)

# Seed DB on startup (remove later in production)
seed_data()


@app.get("/api/v1/overview")
def overview(db: Session = Depends(get_db)):
    total_raised = db.query(func.sum(Candidate.total_raised)).scalar() or 0
    total_spent = db.query(func.sum(Candidate.total_spent)).scalar() or 0

    unique_donors = (
            db.query(func.count(distinct(Donation.donor_name)))
            .filter(Donation.donor_name != "Anonymous")
            .scalar() or 0
    )

    flagged_count = db.query(Candidate).filter(
        Candidate.total_spent > Candidate.legal_spending_limit
    ).count()

    global_total = db.query(func.sum(Donation.amount)).scalar() or 1

    source_query = (
        db.query(Donation.donor_type, func.sum(Donation.amount))
        .group_by(Donation.donor_type)
        .all()
    )

    source_breakdown = [
        {
            "label": donor_type or "Unknown",
            "value": amount,
            "percentage": round((amount / global_total) * 100, 1)
        }
        for donor_type, amount in source_query
    ]

    bar_data = [
        {
            "name": c.full_name,
            "amount": c.total_raised,
            "flagged": c.total_spent > c.legal_spending_limit
        }
        for c in db.query(Candidate).limit(5).all()
    ]

    return {
        "kpi": {
            "total_raised": total_raised,
            "total_spent": total_spent,
            "flagged": flagged_count,
            "donors_count": unique_donors
        },
        "bar_data": bar_data,
        "source_breakdown": source_breakdown
    }


@app.get("/api/v1/candidates")
def list_candidates(db: Session = Depends(get_db)):
    candidates = db.query(Candidate).all()
    results = []
    for c in candidates:
        actual_funding = db.query(func.sum(Donation.amount)).filter(Donation.candidate_id == c.id).scalar() or 0
        status = "Safe"
        if actual_funding > c.legal_spending_limit:
            status = "Over Limit"
        elif actual_funding > (c.legal_spending_limit * 0.9):
            status = "Warning"

        results.append({
            "id": c.id,
            "name": c.full_name,
            "party": c.party.abbreviation if c.party else "IND",
            "office": c.office,
            "total_funding": actual_funding,
            "legal_limit": c.legal_spending_limit,
            "status": status,
            "compliance_pct": round((actual_funding / c.legal_spending_limit) * 100,
                                    1) if c.legal_spending_limit > 0 else 0
        })
    return sorted(results, key=lambda x: x['total_funding'], reverse=True)


@app.get("/api/v1/candidates/{candidate_id}/analysis")
def candidate_analysis(
        candidate_id: int,
        db: Session = Depends(get_db)
):
    candidate = db.query(Candidate).filter_by(id=candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    spending_trends = (
        db.query(
            func.date(Expense.date_incurred).label("date"),
            func.sum(Expense.amount).label("amount")
        )
        .filter(Expense.candidate_id == candidate_id)
        .group_by(func.date(Expense.date_incurred))
        .order_by("date")
        .all()
    )

    top_donors = (
        db.query(
            Donation.donor_name,
            func.sum(Donation.amount).label("total")
        )
        .filter(Donation.candidate_id == candidate_id)
        .group_by(Donation.donor_name)
        .order_by(func.sum(Donation.amount).desc())
        .all()
    )

    flags = []
    if top_donors and (top_donors[0][1] / (candidate.total_raised or 1)) > 0.5:
        flags.append({
            "type": "High Donor Concentration",
            "severity": "Red",
            "detail": f"{top_donors[0][0]} dominates funding"
        })

    return {
        "name": candidate.full_name,
        "line_chart": [{"date": d, "amount": a} for d, a in spending_trends],
        "donor_pie": [{"name": n, "value": v} for n, v in top_donors],
        "comparison_bar": {
            "received": candidate.total_raised,
            "spent": candidate.total_spent,
            "balance": candidate.total_raised - candidate.total_spent
        },
        "risk_flags": flags
    }
