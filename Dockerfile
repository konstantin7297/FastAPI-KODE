FROM python:3.10

RUN apt-get update && rm -rf /var/lib/apt/lists/*

RUN mkdir src/

WORKDIR src/

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY .env .
COPY src/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]