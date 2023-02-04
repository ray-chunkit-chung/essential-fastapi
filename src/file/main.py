import uvicorn
from fastapi import FastAPI, File, UploadFile

import shutil
import os

app = FastAPI()


@app.post("/files/")
async def file(file: bytes = File(...)):
    content = file.decode('utf-8')
    formatfile = content.split('\n')
    return {'filedetail': formatfile}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {'filename': file.filename}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if file:
        filename = file.filename
        fileobj = file.file
        upload_dir = open(os.path.join(UPLOAD_DIR, filename), 'wb+')
        shutil.copyfileobj(fileobj, upload_dir)
        upload_dir.close()
        return {"アップロードファイル名": filename}
    return {"Error": "アップロードファイルが見つかりません。"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
