FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY sample_logs ./sample_logs
COPY pytest.ini .

CMD ["python", "-m", "app.main"]
