#!/usr/bin/python
from SerialReader import SerialReader

ARDUINO_LOCATION = '/dev/ttyACM0'
SERIAL_PORT = 9600

SerialReader(ARDUINO_LOCATION, SERIAL_PORT).startReading()
