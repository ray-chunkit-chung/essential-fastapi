from fastapi import FastAPI, File, UploadFile
from glob import glob

import hashlib
import uvicorn
import shutil
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "local")
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)


# def _hash_md5(file_bytes):
#     """ md5 hash the file bytes"""
#     md5 = hashlib.md5()
#     md5.update(file_bytes[:])
#     return md5.hexdigest()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello file"}


@app.post("/files/")
async def upload_file(file: UploadFile | None = None):
    if file:
        # file_bytes = await file.read()
        # file_md5 = _hash_md5(file_bytes)
        filename = file.filename
        fileobj = file.file
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        return {"filename": filename, "message": "file uploaded successfully"}
    return {"message": "File not found"}


@app.delete("/files/")
async def delete_file(file: UploadFile | None = None):
    if file:
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return {"message": "File deleted successfully"}
    return {"message": "File not found"}


@app.get("/files")
async def get_files():
    abs_paths = glob(os.path.join(UPLOAD_FOLDER, '*'))
    rel_paths = [os.path.relpath(p, UPLOAD_FOLDER) for p in abs_paths]
    return rel_paths


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
