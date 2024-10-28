from fastapi import APIRouter, Depends, HTTPException
from app.server.database import get_db
from asyncpg import Connection
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Item(BaseModel):
    name: str

@router.get("/items", response_model=List[Item])
async def get_items(db: Connection = Depends(get_db)):
    items = await db.fetch("SELECT * FROM items")
    return [Item(name=row['name']) for row in items]

@router.post("/items", response_model=Item)
async def create_item(item: Item, db: Connection = Depends(get_db)):
    try:
        row = await db.fetchrow(
            "INSERT INTO items (name) VALUES ($1) RETURNING *", item.name
        )
        return Item(name=row['name'])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
