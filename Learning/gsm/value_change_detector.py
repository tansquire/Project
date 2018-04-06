#!/usr/bin/python
import time
import mysql.connector
import random
new_stuf_club_value=new_childrenpark_value=new_lakewell_value=new_RR_sump_value=new_actuator_value=old_stuf_club_value=old_childrenpark_value=old_lakewell_value=old_RR_sump_value=old_actuator_value=0
stuff_club_comm_status=childrenpark_comm_status=lakewell_comm_status=RR_sump_comm_status=actuator_comm_status=0
level_prev = time.time()
actuator_prev = time.time()
while(1):
 if(time.time() - level_prev>40+(random.randint(1, 100))/100):
  conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
  mycursor=conn.cursor()
  mycursor.execute("select * FROM AI") 
  list=mycursor.fetchall()
  new_stuf_club_value=list[6][2]
  new_childrenpark_value=list[5][2]
  new_lakewell_value=list[4][2]
  new_RR_sump_value=list[7][2]
  if (new_stuf_club_value != old_stuf_club_value):
   stuff_club_comm_status=1
   old_stuf_club_value = new_stuf_club_value
  else:
   stuff_club_comm_status=0
  if (new_childrenpark_value != old_childrenpark_value):
   childrenpark_comm_status=1
   old_childrenpark_value = new_childrenpark_value
  else:
   childrenpark_comm_status=0
  if (new_lakewell_value != old_lakewell_value):
   lakewell_comm_status=1
   old_lakewell_value = new_lakewell_value
  else:
   lakewell_comm_status=0
  if (new_RR_sump_value != old_RR_sump_value):
   RR_sump_comm_status=1
   old_RR_sump_value = new_RR_sump_value
  else:
   RR_sump_comm_status=0
  mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (lakewell_comm_status, 3))
  mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (childrenpark_comm_status, 4))
  mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (stuff_club_comm_status, 5))
  mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (RR_sump_comm_status, 6))
  print"lakewell, children, stuff_club, RR sump, comm availabilities respectively are=%s, %s, %s, %s"%(lakewell_comm_status,childrenpark_comm_status,stuff_club_comm_status, RR_sump_comm_status)
  conn.commit()
  conn.close()
  mycursor.close()
  level_prev=time.time()
 
 if(time.time() - actuator_prev>10+(random.randint(1, 100))/100):
  conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
  mycursor=conn.cursor()
  mycursor.execute("select * FROM AI") 
  list=mycursor.fetchall()
  new_actuator_value=list[8][2]
  if (new_actuator_value != old_actuator_value):
   actuator_comm_status=1
   print(new_actuator_value)
   old_actuator_value = new_actuator_value
  else:
   actuator_comm_status=0
  mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (actuator_comm_status, 7))
  print"actuator comm availabilities is= %s"%(actuator_comm_status)
  conn.commit()
  conn.close()
  mycursor.close()
  actuator_prev=time.time()
 
 #time.sleep(1)   
#this time must be greater than gate random update time(so gateway freq must be known)
