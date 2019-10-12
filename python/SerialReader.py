#!/usr/bin/python
import serial
from datetime import datetime

ARDUINO_LOCATION = '/dev/ttyACM0'
SERIAL_PORT = 9600

class data:
    

ser = serial.Serial(
    port=ARDUINO_LOCATION,
    baudrate=SERIAL_PORT,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)
while True:
    if ser.isOpen():
        print(datetime.now(), ser.readline())
    else:
        print(datetime.now(), 'Not open')