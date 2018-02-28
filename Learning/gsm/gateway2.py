#!/usr/bin/python
import time
import mysql.connector
import random
data1='667'


def randomsump():
 if len(data1)!=0:
  conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
  mycursor=conn.cursor()
  x=random.randint(1, 500)
  mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (x, 8))
  print"RR sump lora available, random values=%s"%(x)
  conn.commit()
  conn.close()
  mycursor.close()
 else:
  return
 return

while(1):                             
 randomsump()
 time.sleep(1)
