from fastapi import FastAPI, Cookie, Header, Form, File, UploadFile, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field


fake_db = {}


class Item(BaseModel):
    name: str = Field(title="Item Name")
    description: str | None = Field(
        default=None, title="Item description", max_length=300)
    price: float | None = Field(
        default=1, gt=0, description="Item price (>0)")
    tax: float | None = Field(
        default=0., ge=0, description="Tax % (>=0)")
    tags: list | None = Field(
        default=None, title="User-defined tags of this item")


app = FastAPI()


@ app.get("/")
async def root():
    return {"message": "Hello World"}


@ app.get("/items/{name}")
async def read_item(name):
    data = fake_db.get(name, None)
    if not data:
        raise HTTPException(
            status_code=404, detail="404 item not found")
    item = Item(**data)
    return {"item": item}


@ app.post("/items/")
async def create_item(item: Item) -> Item:
    data = jsonable_encoder(item)
    fake_db.update(data)
    return item


@ app.put("/items/{item_id}")
async def update_item(
        item_id: str,
        item: Item | None = None):
    results = {"item_id": item_id}
    if item:
        results.update({"item": item})
    return results


# TODO: Delete
