#!/usr/bin/python
import serial
import time
import mysql.connector
import serial.tools.list_ports
x=serial.tools.list_ports.comports()
for i in range(0,len(x)):
 if('USB' in x[i][0]):
  y=x[i][0]
  print(y)
ser = serial.Serial(y, baudrate = 9600, timeout = 1)
ser = serial.Serial(y, baudrate = 9600, timeout = 1)
ser = serial.Serial(y, baudrate = 9600, timeout = 1)

def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 return data

def opened():
 ser.write(b'c')
 data=ser.readline().decode('ascii')
 return data

def remote():
 ser.write(b'd')
 data=ser.readline().decode('ascii')
 return data


def open():
 conn=mysql.connector.connect(user='root',password='123456',host='localhost',database='test_db')
 mycursor=conn.cursor()
 ser.write(b'a')
 mycursor.execute("UPDATE command SET open= '0' WHERE valve=1")
 conn.commit()
 return

def close():
 conn=mysql.connector.connect(user='root',password='123456',host='localhost',database='test_db')
 mycursor=conn.cursor()
 ser.write(b'b')
 mycursor.execute("UPDATE command SET close= '0' WHERE valve=1")
 conn.commit()
 return


while(1):
 conn=mysql.connector.connect(user='root',password='123456',host='localhost',database='test_db')
 mycursor=conn.cursor()
 mycursor.execute('select * FROM command') 
 list=mycursor.fetchall()
 print(list[0][2])
 print(list[0][1])
 
 time.sleep(2)
 if(list[0][1]=='1'):
  open()
 if(list[0][2]=='1'):
   close()
  
 mycursor.execute("UPDATE command SET opened= %s WHERE valve=1" %(opened()))
 mycursor.execute("UPDATE command SET remote= %s WHERE valve=1" %(remote()))
 conn.commit()


