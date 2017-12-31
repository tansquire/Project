#!/usr/bin/python
import serial
import time
import mysql.connector

ser = serial.Serial('/dev/ttyUSB4', baudrate = 9600, timeout = 0)


def opened():
 ser.write(b'c')
 #time.sleep(8)
 data=ser.readline()
 return data



while(1):
 data=ser.readline().decode('ascii')
 print(data[1][0])

