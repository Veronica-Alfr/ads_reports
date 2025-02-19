FROM python:3.11.10-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "run.py"]