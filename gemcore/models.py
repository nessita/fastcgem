from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    book = Column(String)
    who = Column(String)
    when = Column(DateTime)
    what = Column(String, index=True)
    account = Column(String)
    amount = Column(Float)
    is_income = Column(Boolean, default=False)
    tags = Column(String)
    country = Column(String)
    notes = Column(String)
