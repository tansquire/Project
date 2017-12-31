#!/usr/bin/python
import serial

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 return data


while 1:
 userinput=input('Get data?')
 if(userinput=='y'):
  print(getvalue())
