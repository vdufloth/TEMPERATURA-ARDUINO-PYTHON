#!/usr/bin/python
import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost",
                                     database="temperature",
                                     user="postgres",
                                     password="postgres")

    def insertRegister(self, timestamp, humidity, temperature):
        try:
            """
            print('PostgreSQL database version:')
            cur.execute('SELECT version()')
            db_version = cur.fetchone()
            print(db_version)
            """
            cur = self.conn.cursor()
            insertSql = 'INSERT INTO register(datetime, temperature, humidity) VALUES (%s, %s, %s);'
            cur.execute(insertSql, (timestamp, temperature, humidity))
            self.conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()
                print('Database connection closed.')