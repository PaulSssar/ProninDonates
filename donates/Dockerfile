FROM python:3.11.3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN ls

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]

