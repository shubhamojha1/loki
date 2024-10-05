import os
import time
import logging
import requests
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO) # format add

SERVICE_NAME = os.environ.get('SERVICE_NAME', 'unknown')

@app.route('/health')
def health():
    logging.info(f"{SERVICE_NAME} health check")
    return jsonify({"status": "healthy",
                    "service": SERVICE_NAME})

@app.route('/ping')
def ping():
    logging.info(f"{SERVICE_NAME} received ping")
    return jsonify({"message": "pong", "from": SERVICE_NAME})

def ping_others():
    while True:
        time.sleep(5)
        services = ['service1', 'service2', 'service3', 'service4']
        for service in services:
            try:
                response = requests.get(f"http://{service}:5000/ping")
                logging.info(f"{SERVICE_NAME} pinged {service}: {response.json()}")
            except requests.RequestException as e:
                logging.error(f"{SERVICE_NAME} failed to ping {service}: {str(e)}")

if __name__ == '__main__':
    from threading import Thread
    Thread(target=ping_others, daemon=True).start()
    app.run(host='0.0.0.0', port=5000)