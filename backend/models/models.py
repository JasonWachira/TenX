from sqlalchemy import (
    Column, Integer, String, BigInteger,
    Boolean, DateTime, ForeignKey
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .db import Base


class County(Base):
    __tablename__ = "county"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)

    candidates = relationship("Candidate", back_populates="county")


class Party(Base):
    __tablename__ = "party"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    abbreviation = Column(String(10), unique=True)

    candidates = relationship("Candidate", back_populates="party")


class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    office = Column(String(50), nullable=False)

    county_id = Column(Integer, ForeignKey("county.id"), nullable=True)
    party_id = Column(Integer, ForeignKey("party.id"), nullable=False)

    legal_spending_limit = Column(BigInteger, default=0)
    total_raised = Column(BigInteger, default=0)
    total_spent = Column(BigInteger, default=0)

    county = relationship("County", back_populates="candidates")
    party = relationship("Party", back_populates="candidates")
    donations = relationship("Donation", back_populates="candidate")
    expenses = relationship("Expense", back_populates="candidate")


class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidate.id"), nullable=False)
    amount = Column(BigInteger, nullable=False)

    donor_name = Column(String(150), default="Anonymous")
    donor_type = Column(String(50))
    sector = Column(String(100))
    is_anonymous = Column(Boolean, default=False)
    date_received = Column(DateTime, default=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="donations")


class Expense(Base):
    __tablename__ = "expense"

    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey("candidate.id"), nullable=False)
    amount = Column(BigInteger, nullable=False)

    category = Column(String(100))
    description = Column(String(255))
    date_incurred = Column(DateTime, default=datetime.utcnow)

    candidate = relationship("Candidate", back_populates="expenses")