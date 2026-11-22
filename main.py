import db_control
import time
import board
import adafruit_dht
import RPLCD.i2c import CharLCD

dht = adafruit_dht.DHT22(board.D5)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)

def humidity_sensor():
    humidity_reading = dht.humidity
    return humidity_reading

def temperature_sensor():
    temperature_reading = dht.temperature
    return temperature_reading

def update_lcd(humidity, temperature):
    lcd.clear()
    lcd.write_string(f'Humidity: {humidity:.1f}%')
    lcd.crlf()
    lcd.write_string(f'Temp: {temperature:.1f}C')

db_control.create_table()

while True:
    time.sleep(5)
    humidity = humidity_sensor()
    temperature = temperature_sensor()
    db_control.insert_reading(humidity, temperature)
    update_lcd(humidity, temperature)