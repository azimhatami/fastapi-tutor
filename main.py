from typing import Annotated

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_items(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
):
    results = {
        'item_id': item_id,
        'item': item
    }
    return results
