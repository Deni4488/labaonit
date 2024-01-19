FROM python:3.8-slim
ENV PYTHONDONTWRITEABP 1
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["python", "/app/main.py"]