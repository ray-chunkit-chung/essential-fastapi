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


# Upload files by the client using File as "form data" as bytes in memory
@app.post("/files/")
async def create_file(
        file: bytes = File(),
        token: str = Form()):
    return {"token": token, "file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile,
        token: str = Form()):
    return {"token": token, "filename": file.filename}
# UploadFile: https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile
# Spooled file -- stored in memory up to a maximum size limit, then stored in disk
# metadata, async interface, actual SpooledTemporaryFile object to share as file-like object

# Raise exception


@ app.get("/exceptions/{name}")
async def raise_exception(name):
    if name == "HTTPException":
        raise HTTPException(
            status_code=404, detail="This is 404 HTTPException")
    return {"detail": f"Unknown Exception {name}"}

# TODO: dependency injection https://fastapi.tiangolo.com/tutorial/dependencies/

# TODO: Security https://fastapi.tiangolo.com/tutorial/security/
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/token/")
async def get_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}

# TODO: A "middleware" is a function that works with every request before it is processed by any specific path operation. 
# TODO: CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript code that communicates with a backend, and the backend is in a different "origin" than the frontend.

