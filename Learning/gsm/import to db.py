#!/usr/bin/python
import serial
import time
import mysql.connector
ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)
time.sleep(1)
start = time.time()

def do():
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 while(ser.inWaiting()>0):
  data=ser.readline().decode().split('\r\n')
  #data=ser.readline();
  print(data[0])
  #print(data)
  if('deviceA' in data[0]):
   mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (data[0][9:], 1))
   #print"lakewell data=%s"%(data[0][9:])
  if('deviceB' in data[0]):
   #mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (data[0][9:], 2))
   print"childrenpark data=%s"%(data[0][9:])
 

 conn.commit()
 conn.close()
 mycursor.close() 
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
 #print"lakewell, children, and stuff_club comm availabilities respectively are=%s, %s and %s"%(lake_well_lora_status,childrenpark_lora_status,stuff_club_lora_status)
 conn.close()
 mycursor.close()
 time.sleep(.1)
 end = time.time()
 if(end - start>300 and lake_well_lora_status=='0'):
  ser.write(b'a')
  start=end;

 #if(lake_well_lora_status=='0'):
  #ser.write(b'a')
  #print ("lake well lora fail, command given to lake well")
 do()
 #time.sleep(300)

 #if(childrenpark_lora_status=='0'):
  #ser.write(b'b')
  #print ("children park lora fail, command given to children park")
  #do()
 #time.sleep(60)




