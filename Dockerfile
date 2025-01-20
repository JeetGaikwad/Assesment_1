FROM python:3.9.21-bookworm
COPY . /app
WORKDIR /app
CMD python calculator.py