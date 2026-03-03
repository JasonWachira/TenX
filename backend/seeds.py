from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from models.db import engine, Base, SessionLocal
from models.models import County, Party, Candidate, Donation, Expense


def seed_data():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
        nairobi = County(name="Nairobi")
        mombasa = County(name="Mombasa")

        db.add_all([nairobi, mombasa])
        db.commit()

        party_a = Party(name="Azimio la Umoja", abbreviation="AZM")
        party_b = Party(name="Kenya Kwanza", abbreviation="KK")

        db.add_all([party_a, party_b])
        db.commit()

        pres_cand = Candidate(
            full_name="Alpha Candidate",
            office="Presidential",
            party_id=party_a.id,
            legal_spending_limit=4_400_000_000,
            total_raised=1_200_000_000,
            total_spent=950_000_000
        )

        db.add(pres_cand)
        db.commit()

        donations = [
            Donation(
                candidate_id=pres_cand.id,
                amount=50_000_000,
                donor_name="Construction Corp",
                donor_type="Corporate",
                sector="Infrastructure"
            ),
            Donation(
                candidate_id=pres_cand.id,
                amount=300_000_000,
                donor_name="Anonymous",
                is_anonymous=True,
                sector="Unknown"
            ),
            Donation(
                candidate_id=pres_cand.id,
                amount=12_000_000,
                donor_name="Banking Bank",
                donor_type="Corporate",
                sector="Finance"
            )
        ]

        expenses = [
            Expense(
                candidate_id=pres_cand.id,
                amount=200_000_000,
                category="Media Ads",
                description="TV & Billboard Campaign"
            ),
            Expense(
                candidate_id=pres_cand.id,
                amount=500_000_000,
                category="Logistics",
                description="Helicopter & Ground Transport",
                date_incurred=datetime.utcnow() - timedelta(days=2)
            )
        ]

        db.add_all(donations + expenses)
        db.commit()

        print("Database seeded successfully")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()