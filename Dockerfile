# backend/Dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8081
CMD ["python", "app.py"]