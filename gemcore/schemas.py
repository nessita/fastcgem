from datetime import date
from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    book: str
    who: Optional[str] = None
    when: Optional[date] = None
    what: str
    account: str
    amount: Decimal
    is_income: bool = False
    tags: str
    country: str
    notes: Optional[str] = ''


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
