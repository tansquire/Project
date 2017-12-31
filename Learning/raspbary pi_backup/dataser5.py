#!/usr/bin/python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 return data


while 1:
  f=open('/var/www/html/php.txt','w')
  f.write(getvalue())
  f.close()
  time.sleep(2)
