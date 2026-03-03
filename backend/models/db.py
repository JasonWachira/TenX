from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class County(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    candidates = db.relationship('Candidate', backref='county', lazy=True)


class Party(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    abbreviation = db.Column(db.String(10), unique=True)
    candidates = db.relationship('Candidate', backref='party', lazy=True)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    office = db.Column(db.String(50), nullable=False)

    county_id = db.Column(db.Integer, db.ForeignKey('county.id'), nullable=True)
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'), nullable=False)

    legal_spending_limit = db.Column(db.BigInteger, default=0)
    total_raised = db.Column(db.BigInteger, default=0)
    total_spent = db.Column(db.BigInteger, default=0)

    donations = db.relationship('Donation', backref='candidate', lazy=True)
    expenses = db.relationship('Expense', backref='candidate', lazy=True)


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    donor_name = db.Column(db.String(150), default="Anonymous")
    donor_type = db.Column(db.String(50))
    sector = db.Column(db.String(100))
    is_anonymous = db.Column(db.Boolean, default=False)
    date_received = db.Column(db.DateTime, default=datetime.utcnow)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    amount = db.Column(db.BigInteger, nullable=False)
    category = db.Column(db.String(100))
    description = db.Column(db.String(255))
    date_incurred = db.Column(db.DateTime, default=datetime.utcnow)

