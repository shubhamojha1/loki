FROM python:3.9-slim

WORKDIR /app

COPY service.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "service.py"]