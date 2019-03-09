#!/usr/bin/python
import serial
import time
import datetime

while(1):
 try:
  ser=serial.Serial('/dev/ttyACM0', baudrate=9600)
  data=ser.readline()
  currentDT=datetime.datetime.now()
  print(str(currentDT))
  print("water line pressure at farthest point=%s kg/cm2" %data)
 #print(data)
  time.sleep(1)
 except:
  print("error") 
