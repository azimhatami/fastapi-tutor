from typing import Annotated

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title='The description of the time', max_length=300
    )
    price: float = Field(
        gt=0, description='The price must be greater than zero'
    )
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
