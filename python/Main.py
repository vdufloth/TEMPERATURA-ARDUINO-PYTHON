#!/usr/bin/python
from ArduinoInterface import SerialReader
from DatabaseInterface import Database
from time import sleep
SerialReader().start()

db = Database()
while True:
    rows = db.getRegisters()
    for row in rows:
        print('id', row[0], 'datetime', row[1], 'temperature', row[2], 'humidity', row[3])
    sleep(5)