# Day 10 — ESP8266 REST Client (Simulation Mode)

## 🎯 Objective

Simulate an ESP8266 IoT device sending sensor data to a Flask REST API and storing it in SQLite.

---

## 🏗️ System Architecture

```
Simulated ESP8266 (Python Script)
            ↓ HTTP POST
        Flask REST API
            ↓
      SQLite Database
```

---

## 📦 What is Simulated?

Instead of real hardware:

* Python script acts as ESP8266
* Generates fake sensor data
* Sends HTTP requests to API

---

## 🧠 Key Concepts Learned

* IoT device communication
* REST API client-side usage
* HTTP POST requests from devices
* Sensor data simulation
* Client-server architecture
* IoT pipeline design

---

## 📁 Project Structure

```
python/
  api.py → Flask REST API server
  db.py → SQLite database logic
  sim_device.py → ESP8266 simulator

esp8266/
  device_reporter.ino → future real firmware
```

---

## 🚀 How to Run

### 1. Start API

```
python python/api.py
```

### 2. Run simulated device

```
python python/sim_device.py
```

---

## 📡 Expected Flow

1. Simulated device generates data
2. Sends POST request to API
3. API stores data in SQLite
4. System logs device activity

---

## 🔥 Learning Outcome

You built your first IoT pipeline:

* Device → API → Database

This is the foundation of real IoT systems used in industry.
