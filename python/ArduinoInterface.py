#!/usr/bin/python
import serial
from DatabaseInterface import Database
from datetime import datetime

class DataRead:
    def __init__(self, timestamp, humidity, temperature):
        self.timestamp = timestamp
        self.humidity = humidity
        self.temperature = temperature

class SerialReader:
    def __init__(self, ArduinoLocation, SerialPort):
        self.ArduinoLocation = ArduinoLocation
        self.SerialPort = SerialPort
        self.ser = serial.Serial(
            port=self.ArduinoLocation,
            baudrate=self.SerialPort,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS
        )
        self.db = Database()

    def startReading(self):
        if True:
            if self.ser.isOpen():
                lineRead = self.ser.readline().decode("utf-8").split(sep=";")
                dt = DataRead(datetime.now(), lineRead[0], lineRead[1])
                self.db.insertRegister(dt.timestamp, dt.humidity, dt.temperature)
            else:
                print(datetime.now(), 'Not open')