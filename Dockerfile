FROM python:3.8
COPY roll_witch /app/roll_witch
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3", "-m", "roll_witch.main"]
