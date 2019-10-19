#!/usr/bin/python
import psycopg2

HOST='localhost'
DATABASE='temperature'
USER='postgres'
PASSWORD='postgres'


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                Database._instance.connection = psycopg2.connect(host=HOST,
                                                                 database=DATABASE,
                                                                 user=USER,
                                                                 password=PASSWORD)
                Database._instance.cursor = Database._instance.connection.cursor()
                print('Nova conexao com banco criada')

            except Exception as error:
                print('Erro ao criar conexao', error)
                Database._instance = None

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def insertRegister(self, timestamp, humidity, temperature):
        try:
            print("Inserindo registro")
            insertSql = 'INSERT INTO register(datetime, temperature, humidity) VALUES (%s, %s, %s);'
            self.cursor.execute(insertSql, (timestamp, temperature, humidity))
            self.connection.commit()
            print("Registro inserido")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Não foi posível inserir registro. Erro:", error)

    def getRegisters(self):
        try:
            print("Buscando registros no banco")
            selectSql = 'SELECT * FROM register;'
            self.cursor.execute(selectSql)
            return self.cursor.fetchall()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Não foi posível buscar os registros. Erro:", error)

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        print("Conexão com o banco fechada")