#!/usr/bin/python
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
while 1:
 data=ser.readline()
 print(data)

