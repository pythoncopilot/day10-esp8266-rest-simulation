/*
=====================================================
 ESP8266 IoT Device - Production Template (Day 10)
=====================================================

PURPOSE:
This firmware is designed for real ESP8266 hardware.

It replaces the Python simulator (sim_device.py).

-----------------------------------------------------
 HOW TO USE (IMPORTANT)
-----------------------------------------------------

STEP 1:
Replace WiFi credentials below.

STEP 2:
Replace API endpoint with your server IP:

Example:
http://192.168.1.100:5000/devices

STEP 3:
Upload to ESP8266 using Arduino IDE.

STEP 4:
Ensure Flask API is running on same network.

-----------------------------------------------------
 WHAT THIS DEVICE DOES
-----------------------------------------------------

- Connects to WiFi
- Sends sensor data via HTTP POST
- Simulates temperature sensor
- Sends data every 5 seconds

-----------------------------------------------------
 WHEN MOVING FROM SIMULATION → REAL HARDWARE
-----------------------------------------------------

You must:
1. Stop using sim_device.py
2. Use THIS firmware instead
3. Keep API and DB unchanged
4. Only update endpoint IP

=====================================================
*/

#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "YOUR_WIFI_NAME";
const char* password = "YOUR_WIFI_PASSWORD";

// Change this to your Flask server IP
const char* serverUrl = "http://YOUR_SERVER_IP:5000/devices";

String deviceID = "ESP8266_NODE_01";

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi!");
}

void loop() {

  if (WiFi.status() == WL_CONNECTED) {

    WiFiClient client;
    HTTPClient http;

    http.begin(client, serverUrl);
    http.addHeader("Content-Type", "application/json");

    float temperature = random(200, 350) / 10.0;

    String payload = "{";
    payload += "\"name\":\"" + deviceID + "\",";
    payload += "\"status\":\"online\",";
    payload += "\"temperature\":" + String(temperature);
    payload += "}";

    int httpResponseCode = http.POST(payload);

    Serial.print("HTTP Response: ");
    Serial.println(httpResponseCode);

    http.end();
  }

  delay(5000);
}