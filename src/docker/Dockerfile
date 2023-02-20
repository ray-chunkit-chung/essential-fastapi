FROM python:3.11
WORKDIR /workspace
COPY ./requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /workspace/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Test local
# uvicorn main:app --reload