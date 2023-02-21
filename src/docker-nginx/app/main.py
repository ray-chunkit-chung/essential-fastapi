from fastapi import FastAPI

DUMMY_ITEMS = [{"item_name": "Foo"}, {
    "item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World docker-nginx"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/queries/")
async def query(skip: int = 0, limit: int = 10):
    return DUMMY_ITEMS[skip: skip + limit]
