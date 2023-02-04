from fastapi import FastAPI, Cookie, Header, Form
from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str = Field(title="Item Name")
    description: str | None = Field(
        default=None, title="Item description ", max_length=300)
    price: float | None = Field(
        default=1, gt=0, description="Item price (>0)")
    tax: float | None = Field(
        default=0., ge=0, description="Tax % (>=0)")
    tags: list | None = Field(
        default=None, title="User-defined tags")


app = FastAPI()


@ app.get("/")
async def root():
    return {"message": "Hello World"}


@ app.get("/items/{name}")
async def read_item(name):
    return {"item_name": name}


@ app.post("/items/")
async def create_item(item: Item) -> Item:
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


@ app.get("/cookies/")
async def read_cookie(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


@ app.get("/headers/")
async def read_header(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}


# When you need to receive form fields instead of JSON, you can use Form
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
