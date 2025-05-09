FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY flask_app.py .
COPY scripts/ ./scripts/

EXPOSE 10000

CMD ["gunicorn", "flask_app:app", "--workers", "1", "--worker-class", "sync", "--bind", "0.0.0.0:10000"]
