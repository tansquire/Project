#!/usr/bin/python

import serial
import time
import mysql.connector
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 return data

conn=mysql.connector.connect(user='root',password='123456',host='10.22.52.214',database='test_db')
mycursor=conn.cursor()
mycursor.execute('show tables')
print(mycursor.fetchall())

while 1:
 time.sleep(2)
 x=getvalue()
 mycursor.execute("UPDATE student SET roll= %s WHERE idstudent=10" %(x))
 conn.commit()
