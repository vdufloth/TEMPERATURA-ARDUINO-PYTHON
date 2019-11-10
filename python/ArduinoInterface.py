from threading import Thread
import serial
from datetime import datetime
import requests
import json

ARDUINO_LOCATION = '/dev/ttyACM0'
SERIAL_PORT = 9600
POST_URL = 'http://192.168.0.99/sist-distribuidos/api/data.php'


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
            self.keepReading = True
        except Exception as error:
            print('Erro ao conectar com arduino', error)
            self.keepReading = False

    def run(self):
        print('Iniciando leitura')
        while self.keepReading:
            if self.ser.isOpen():
                lineRead = self.ser.readline().decode("utf-8").split(sep=";")
                time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                register = json.dumps({'readtime': time,
                                       'humidity': lineRead[0],
                                       'temperature': lineRead[1],
                                       })
                print('Enviando', register, 'para', POST_URL)
                try:
                    result = requests.post(POST_URL, data=register)
                    print('Post result:', result.text)
                except Exception as error:
                    print('Erro ao enviar:', error)
            else:
                print('Porta serial nao aberta:', datetime.now())

    def stopReading(self):
        print('Parando leitura')
        self.keepReading = False

    def restartReading(self):
        print('Reiniciando leitura')
        self.keepReading = True

    def setReadingInterval(self, seconds):
        print('Alterando intervalo de leitura no Arduino para', seconds, 'segundos')
        # Pass to arduino
