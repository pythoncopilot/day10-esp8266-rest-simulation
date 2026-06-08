from flask import Flask, request, jsonify
import db

app = Flask(__name__)

db.init_db()


def response(success, data=None, error=None):
    return {"success": success, "data": data, "error": error}


@app.route("/")
def home():
    return jsonify(response(True, "Day 10 ESP8266 Simulation API"))


@app.route("/devices", methods=["POST"])
def add_device():
    data = request.json

    if not data:
        return jsonify(response(False, error="No data provided")), 400

    name = data.get("name")
    status = data.get("status")
    temperature = data.get("temperature")

    if not name:
        return jsonify(response(False, error="Missing device name")), 400

    db.add_device(name, status, temperature)

    return jsonify(response(True, "Data stored")), 201


@app.route("/devices", methods=["GET"])
def get_devices():
    rows = db.get_devices()
    result = []

    for r in rows:
        result.append({
            "id": r[0],
            "name": r[1],
            "status": r[2],
            "temperature": r[3],
            "timestamp": r[4]
        })

    return jsonify(response(True, result))


if __name__ == "__main__":
    app.run(debug=True)