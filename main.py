from datetime import datetime
from decimal import Decimal
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    book: str
    who: Optional[str] = None
    when: Optional[datetime] = None
    what: str
    account: str
    description: Optional[str] = None
    amount: Decimal
    tags: str
    country: str
    notes: Optional[str] = ''


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/items/")
async def create_item(item: Item):
    return item
