import sqlite3

connection = sqlite3.connect('database/sensor_readings.db')

cursor = connection.cursor()

def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_readings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        humidity REAL,
                        temperature REAL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )''')
    connection.commit()

def insert_reading(humidity, temperature):
    cursor.execute('''INSERT INTO sensor_readings (humidity, temperature) 
                      VALUES (?, ?)''', (humidity, temperature))
    connection.commit()