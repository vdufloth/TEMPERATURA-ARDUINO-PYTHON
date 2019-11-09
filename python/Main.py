#!/usr/bin/python3
from ArduinoInterface import SerialReader
from time import sleep

sr = SerialReader()
sr.start()
sleep(10)
sr.stopReading()
sleep(2)
sr.restartReading