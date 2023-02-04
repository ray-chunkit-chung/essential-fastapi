from fastapi import FastAPI

DUMMY_DATA = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World v4"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/queries/")
async def query(skip: int = 0, limit: int = 10):
    return DUMMY_DATA[skip: skip + limit]
