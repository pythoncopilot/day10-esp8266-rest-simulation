# Day 10 — ESP8266 REST Simulation + Hardware Ready IoT System

## 🚀 Overview

This project simulates an IoT system where a device sends sensor data to a Flask REST API and stores it in SQLite.

It supports two modes:

- Simulation Mode (Python-based ESP8266 simulator)
- Hardware Mode (Real ESP8266 firmware)

---

## 🏗️ System Architecture

### Simulation Mode
Simulated Device (Python)
        ↓ HTTP POST
Flask REST API
        ↓
SQLite Database

---

### Hardware Mode
ESP8266 (Arduino Firmware)
        ↓ HTTP POST
Flask REST API
        ↓
SQLite Database

---

## 📁 Project Structure

python/
- api.py              → Flask REST API server
- db.py               → SQLite database logic
- sim_device.py       → ESP8266 simulator (Python)

arduino/
- esp8266_device.ino  → Real ESP8266 firmware (production ready)

database/
- inventory.db

.github/
- workflows/
  - ci.yml

---

## 🧠 Key Concepts Learned

- IoT device simulation
- REST API communication (HTTP POST)
- Flask backend development
- SQLite database integration
- Client-server architecture
- Hardware vs simulation abstraction
- Embedded system networking basics

---

## 🔧 API Endpoints

### POST /devices
Stores IoT device data

Example payload:
{
  "name": "ESP_SIM_01",
  "status": "online",
  "temperature": 25.5
}

---

### GET /devices
Returns all stored device data

---

## 🧪 How to Run (Simulation Mode)

### Step 1 — Start API
python python/api.py

### Step 2 — Run simulator
python python/sim_device.py

---

## 🤖 Hardware Integration (ESP8266)

### Firmware Location
arduino/esp8266_device.ino

### How to switch to hardware mode:

1. Flash ESP8266 using Arduino IDE
2. Update WiFi credentials in .ino file
3. Update server IP address:
   http://YOUR_SERVER_IP:5000/devices
4. Stop Python simulator

---

## 🔄 Architecture Modes

Simulation Mode:
Python Simulator → Flask API → SQLite

Hardware Mode:
ESP8266 Device → Flask API → SQLite

Backend remains unchanged in both modes.

---

## 🎯 Learning Outcomes

- Built full IoT data pipeline
- Understood REST-based IoT communication
- Learned device vs server separation
- Practiced hardware abstraction design
- Prepared system for real embedded deployment

---

## 🚀 Future Enhancements

- Multi-device simulation
- MQTT integration
- Real-time dashboard
- Device command system (API → ESP control)
- WebSocket live updates