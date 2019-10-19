#!/usr/bin/python
import serial
from DatabaseInterface import Database
from datetime import datetime
from threading import Thread

ARDUINO_LOCATION = '/dev/ttyACM0'
SERIAL_PORT = 9600


class SerialReader(Thread):
    def __init__(self):
        Thread.__init__(self)
        try:
            self.ArduinoLocation = ARDUINO_LOCATION
            self.SerialPort = SERIAL_PORT
            self.ser = serial.Serial(
                port=self.ArduinoLocation,
                baudrate=self.SerialPort,
                parity=serial.PARITY_ODD,
                stopbits=serial.STOPBITS_TWO,
                bytesize=serial.SEVENBITS
            )
            self.db = Database()
            self.keepReading = True
        except Exception as error:
            print('Erro ao conectar com arduino', error)
            self.keepReading = False

    def run(self):
        while self.keepReading:
            if self.ser.isOpen():
                lineRead = self.ser.readline().decode("utf-8").split(sep=";")
                time = datetime.now()
                print("Registro capturado:", time, lineRead[0], lineRead[1])
                self.db.insertRegister(time, lineRead[0], lineRead[1])
            else:
                print('Porta serial não aberta:', datetime.now())