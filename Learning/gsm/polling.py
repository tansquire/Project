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
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("select * FROM DI where id=3") 
 list=mycursor.fetchall()
 lake_well_lora_status=(list[0][2])
 mycursor.execute("select * FROM DI where id=4") 
 list=mycursor.fetchall()
 childrenpark_lora_status=(list[0][2])
 mycursor.execute("select * FROM DI where id=5") 
 list=mycursor.fetchall()
 stuff_club_lora_status=(list[0][2])
 print"lakewell, children, and stuff_club comm availabilities respectively are=%s, %s and %s"%(lake_well_lora_status,childrenpark_lora_status,stuff_club_lora_status)
 conn.close()
 mycursor.close()
 time.sleep(1)

 if(lake_well_lora_status=='0'):
  ser.write(b'a')
  print 'lake well lora fail, command given to lake well'
  do()
 time.sleep(30)

 if(childrenpark_lora_status=='0'):
  ser.write(b'b')
  print ("children park lora fail, command given to children park")
  do()
 time.sleep(30)


