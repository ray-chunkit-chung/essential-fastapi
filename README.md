# essential-fastapi

## Step1 Install python

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3 python3-dev python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade -r requirements.txt
```

If windows,

```cmd
.venv/Scripts/activate
```

## App1 hello world app

<https://fastapi.tiangolo.com/tutorial/first-steps/>

```bash
cd src/hello_world
uvicorn main:app --reload
```

The app root is <http://127.0.0.1:8000/>
The path parameter is <http://127.0.0.1:8000/items/my-variable>
The query parameter is <http://127.0.0.1:8000/queries/?skip=1&limit=1>

The api doc is at <http://localhost:8000/docs> provided by <https://github.com/swagger-api/swagger-ui>

Another api doc is at
<http://127.0.0.1:8000/redoc> provided by <https://github.com/Redocly/redoc>

## App2 restful

```bash
cd src/restful
uvicorn main:app --reload
```

## App3 upload, download, delete files

<https://senablog.com/python-fastapi-file-upload/>

Coming soon...

## App4 video streaming

<https://koding.work/video-streaming-with-opencv-flask/>

Coming soon...

## App5 bigger app <https://fastapi.tiangolo.com/tutorial/bigger-applications/>

## Trouble shooting

Fatal detected dubious ownership in repository at '/com.docker.devenvironments.code'

```bash
git config --global --add safe.directory /com.docker.devenvironments.code
```
