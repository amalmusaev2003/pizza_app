FROM python:3.10-slim

WORKDIR /pizza_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bnd=0.0.0.0:8000"]
