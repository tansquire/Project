#!/usr/bin/python
import serial
import time
import mysql.connector
ser = serial.Serial('/dev/ttyACM1', baudrate = 9600, timeout = 1)
def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 return data



def open():
 conn=mysql.connector.connect(user='root',password='123456',host='localhost',database='test_db')
 mycursor=conn.cursor()
 ser.write(b'a')
 mycursor.execute("UPDATE command SET open= '0' WHERE valve=1")
 conn.commit()
 return





conn=mysql.connector.connect(user='root',password='123456',host='localhost',database='test_db')
mycursor=conn.cursor()
mycursor.execute('select * FROM command') 
list=mycursor.fetchall()
print(list[0][1])
open()
 
