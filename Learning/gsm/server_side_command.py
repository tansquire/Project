#!/usr/bin/python
import serial
import time
import mysql.connector
from time import gmtime, strftime
from datetime import datetime
ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600)
time.sleep(1)
lake_well_command_prev = time.time()
children_park_command_prev=time.time()
stuff_club_command_prev=time.time()
RR_sump_command_prev=time.time()
actuator_open_command_prev=time.time()
actuator_close_command_prev=time.time()
any_command_prev=time.time()
count=0

while(1):
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("select * FROM DI") 
 list=mycursor.fetchall()
 lake_well_lora_status=(list[2][2])
 childrenpark_lora_status=(list[3][2])
 stuff_club_lora_status=(list[4][2])
 RR_sump_lora_status=(list[5][2])
 actuator_lora_status=(list[6][2])
 
 mycursor.execute("select * FROM DO") 
 list=mycursor.fetchall()
 open_command=(list[2][2])
 close_command=(list[3][2])
 lake_well_command=(list[4][2])
 children_park_command=(list[5][2])
 stuff_club_command=(list[6][2])
 RR_sump_command=(list[7][2])
 

 #print"lakewell, children, and stuff_club, RR sump, and actuator comm availabilities respectively are=%s, %s, %s, %s and %s"%(lake_well_lora_status,childrenpark_lora_status,stuff_club_lora_status,RR_sump_lora_status, actuator_lora_status )

 if(ser.inWaiting()>0):
  data=ser.readline()
  print(data)
  if('SMS sent' in data):
   count=count+1
   print(count)
 
 if(time.time() - lake_well_command_prev>900 and time.time() - any_command_prev>20 and lake_well_lora_status=='0'):
  print datetime.now()
  ser.write(b'l')
  print('data request to lake well')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'data request to lake well'))  
  lake_well_command_prev=time.time()
  any_command_prev=time.time()
 
 if(time.time() - children_park_command_prev>900 and time.time() - any_command_prev>20 and childrenpark_lora_status=='0'):
  print datetime.now()
  ser.write(b'c')
  print('data request to children park')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'data request to children park'))  
  children_park_command_prev=time.time()
  any_command_prev=time.time()

 if(time.time() - stuff_club_command_prev>900 and time.time() - any_command_prev>20 and stuff_club_lora_status=='0'):
  print datetime.now()
  ser.write(b's')
  print('data request to stuff club')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'data request to stuff club'))  
  stuff_club_command_prev=time.time()
  any_command_prev=time.time()

 if(time.time() - RR_sump_command_prev>900 and time.time() - any_command_prev>20 and RR_sump_lora_status=='0'):
  print datetime.now()
  ser.write(b'r')
  print('data request to RR sump')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'data request to RR sump'))  
  RR_sump_command_prev=time.time()
  any_command_prev=time.time()

 if(time.time() - actuator_open_command_prev>15 and time.time() - any_command_prev>10 and actuator_lora_status=='0' and open_command=='1'):
  print datetime.now()
  ser.write(b'x')
  print('open command given to actuator')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'open command given to actuator'))  
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 3))
  actuator_open_command_prev=time.time()
  any_command_prev=time.time()

 if(time.time() - actuator_close_command_prev>15 and time.time() - any_command_prev>10 and actuator_lora_status=='0' and close_command=='1'):
  print datetime.now()
  ser.write(b'y')
  print('close command given to actuator')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'close command given to actuator'))  
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 4))
  actuator_close_command_prev=time.time()
  any_command_prev=time.time()


 if(actuator_lora_status=='1' and open_command=='1'):
  print datetime.now()
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('1', 1))
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 3))
  print('open command given to actuator through primary link')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'open command given to actuator through primary link'))  

 if(actuator_lora_status=='1' and close_command=='1'):
  print datetime.now()
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('1', 2))
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 4))
  print('open command given to actuator through primary link')
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'open command given to actuator through primary link')) 

 if(time.time() - any_command_prev>13 and lake_well_command=='1'):
  print datetime.now()
  ser.write(b'l')
  print('manual data request to lake well')
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 5))
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'manual data request to lake well'))  
  any_command_prev=time.time()

 if(time.time() - any_command_prev>13 and children_park_command=='1'):
  print datetime.now()
  ser.write(b'c')
  print('manual data request to children park')
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 6))
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'manual data request to lchildren park'))  
  any_command_prev=time.time()
 
 if(time.time() - any_command_prev>13 and stuff_club_command=='1'):
  print datetime.now()
  ser.write(b's')
  print('manual data request to stuf club')
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 7))
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'manual data request to stuf club'))  
  any_command_prev=time.time()

 if(time.time() - any_command_prev>13 and RR_sump_command=='1'):
  print datetime.now()
  ser.write(b'r')
  print('manual data request to RR sump')
  mycursor.execute("UPDATE DO SET value='%s'WHERE id='%s'" % ('0', 8))
  mycursor.execute("insert into gsm_test (id, name,value) values (%d, '%s', '%s')" % (1, datetime.now(),'manual data request to RR sump'))  
  any_command_prev=time.time()

 conn.commit()
 conn.close()
 mycursor.close() 
time.sleep(.1)
