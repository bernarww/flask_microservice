FROM python:3.12
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src .
EXPOSE 5000
CMD ["python", "app.py"]
# docker-compose up --build -d