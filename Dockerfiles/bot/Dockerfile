FROM python:3.13

WORKDIR /app/bot

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "run.py"]