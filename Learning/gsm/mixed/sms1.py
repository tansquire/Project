
#!/usr/bin/python
import serial
import time
import mysql.connector
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600)
time.sleep(3)
while(1):
 if(ser.inWaiting()>0):
  #data=ser.readline().decode().split('\r\n')
  data=ser.readline()
  #if (data[0]=='+917602304567'):
   #print(data[0])
  #if('+917602304567' in data):
   #data1=data
  #if('.' in data):
   #data2=data
  #data3=data1+data2
  print(data)
  #print("Received data")
 #else:
  #print('Please wait..')
 
 time.sleep(.1)







