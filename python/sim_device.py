import requests
import time
import random

API = "http://127.0.0.1:5000/devices"

DEVICE_ID = "ESP_SIM_01"


def generate():
    return {
        "name": DEVICE_ID,
        "status": "online",
        "temperature": round(random.uniform(20, 35), 2)
    }


while True:
    data = generate()

    try:
        res = requests.post(API, json=data)
        print("Sent:", data)
        print("Response:", res.json())
    except Exception as e:
        print("Error:", e)

    time.sleep(3)