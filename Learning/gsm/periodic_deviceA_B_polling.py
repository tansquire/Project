
#!/usr/bin/python
import serial
import time
import mysql.connector
ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)
time.sleep(3)


def do():
 while(ser.inWaiting()>0):
  data=ser.readline().decode().split('\r\n')
  print(data[0])
 return

while(1):
  ser.write(b'a')
  do()
  time.sleep(30)
  ser.write(b'b')
  do()
  time.sleep(30)



