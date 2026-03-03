from .db import *
from datetime import datetime, timedelta


def seed_data():
    db.drop_all()
    db.create_all()

    nairobi = County(name="Nairobi")
    mombasa = County(name="Mombasa")
    db.session.add_all([nairobi, mombasa])

    party_a = Party(name="Azimio la Umoja", abbreviation="AZM")
    party_b = Party(name="Kenya Kwanza", abbreviation="KK")
    db.session.add_all([party_a, party_b])
    db.session.commit()

    pres_cand = Candidate(
        full_name="Alpha Candidate",
        office="Presidential",
        party_id=party_a.id,
        legal_spending_limit=4400000000,
        total_raised=1200000000,
        total_spent=950000000
    )
    db.session.add(pres_cand)
    db.session.commit()

    donations = [
        Donation(candidate_id=pres_cand.id, amount=50000000, donor_name="Construction Corp",
                 sector="Infrastructure", donor_type="Corporate"),
        Donation(candidate_id=pres_cand.id, amount=300000000, donor_name="Anonymous", is_anonymous=True,
                 sector="Unknown")  # Risk: High Anon
    ]

    expenses = [
        Expense(candidate_id=pres_cand.id, amount=200000000, category="Media Ads",
                description="TV & Billboard Campaign"),
        Expense(candidate_id=pres_cand.id, amount=500000000, category="Logistics",
                description="Helicopter & Ground Transport",
                date_incurred=datetime.utcnow() - timedelta(days=2))  # Spike near "today"
    ]

    db.session.add_all(donations + expenses)
    db.session.commit()
    print("Database Seeded Successfully!")


if __name__ == "__main__":
    seed_data()
