import sqlite3
from datetime import datetime

DB = "database/inventory.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT,
            temperature REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_device(name, status, temperature):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
        INSERT INTO devices (name, status, temperature, timestamp)
        VALUES (?, ?, ?, ?)
    """, (
        name,
        status,
        temperature,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_devices():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("SELECT * FROM devices")
    rows = c.fetchall()

    conn.close()
    return rows