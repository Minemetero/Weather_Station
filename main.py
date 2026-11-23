import db_control
import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

dht = adafruit_dht.DHT22(board.D5) # Humidity/Temp sensore
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8) #LCD Screen

def humidity_sensor():
    humidity_reading = dht.humidity
    return humidity_reading

def temperature_sensor():
    temperature_reading = dht.temperature
    return temperature_reading

def update_lcd(humidity, temperature):
    """
    Update the LCD screen with humidity and temperature readings.

    Parameters
    ----------
    humidity : float
        Just humidity reading from the sensor.
    temperature : float
        Like how it's named.
    """
    lcd.clear()
    lcd.write_string(f'Humidity: {humidity:.1f}%') #This is much better but less flexible ig.
    lcd.crlf()
    lcd.write_string(f'Temp: {temperature:.1f}C') #tbh, I don't even know if it returns float or int.

# Database is created if it doesn't exist.
db_control.create_table()

while True:
    time.sleep(5) #Change this value for sampling rate
    humidity = humidity_sensor()
    temperature = temperature_sensor()
    db_control.insert_reading(humidity, temperature)
    update_lcd(humidity, temperature)