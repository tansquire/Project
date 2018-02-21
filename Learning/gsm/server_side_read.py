#!/usr/bin/python
import serial
import time
import mysql.connector
from time import gmtime, strftime
from datetime import datetime
ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)
time.sleep(1)
start = time.time()

while(1):
 
 if(ser.inWaiting()>0):
  data=ser.readline()
  print(data)
  if('@' in data and '#' in data):
   data1=data.decode().split('\r\n')
   print(data1[0])
   if('actuator' in data1[0]):
    remote=int(data1[0][19])-6
    opd=int(data1[0][20])-6
    cld=int(data1[0][21])-6
    print(remote)
    print(opd)
    print(cld)
   if('deviceA' in data1[0]):
    deviceA_data=data[0][data[0].find('<')+1:data[0].find('>')]
    print(deviceA_data)
   
 
  
 time.sleep(.1)
