#!/usr/bin/python
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)
# ser.write(b'5')
print("Valores Registrados:")
print(ser.read())