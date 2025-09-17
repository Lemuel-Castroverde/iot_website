import sqlite3

DB_FILE = "sensors.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    """Create all required tables if they don't exist."""
    conn = get_connection()
    c = conn.cursor()
    # Table for Act01 (Temp & Humidity)
    c.execute("""
        CREATE TABLE IF NOT EXISTS temp_humidity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            temperature REAL,
            humidity REAL
        )
    """)
    conn.commit()
    conn.close()

def insert_temp_humidity(timestamp, temperature, humidity):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO temp_humidity (timestamp, temperature, humidity) VALUES (?, ?, ?)",
              (timestamp, temperature, humidity))
    conn.commit()
    conn.close()

def get_temp_humidity_minutes():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT DISTINCT strftime('%Y-%m-%d %H:%M', datetime(timestamp, 'unixepoch')) as minute
        FROM temp_humidity ORDER BY minute DESC
    """)
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]

def get_temp_humidity_history(minute):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT timestamp, temperature, humidity 
        FROM temp_humidity
        WHERE strftime('%Y-%m-%d %H:%M', datetime(timestamp, 'unixepoch')) = ?
        ORDER BY timestamp ASC
    """, (minute,))
    rows = c.fetchall()
    conn.close()
    return [{"time": ts, "temperature": temp, "humidity": hum} for ts, temp, hum in rows]
