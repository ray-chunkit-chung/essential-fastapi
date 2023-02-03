# essential-fastapi

<https://senablog.com/python-fastapi-file-upload/>

## Step1 Hello world app

### Step1.1 Install python

```bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3 python3-dev python3-venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Step1.2 Hello world app

```bash
cd src/hello_world
uvicorn main:app --reload
```

## Trouble shooting

Fatal detected dubious ownership in repository at '/com.docker.devenvironments.code'

```bash
git config --global --add safe.directory /com.docker.devenvironments.code
```
