#!/usr/bin/python
import time
import mysql.connector
import random
#data=""
#data='$4#26.2'                    #for stuff club             
#data='$3#26.2#4#10.2'             #stuf club and children park
data='$2#30.2#3#26.2#4#70.2'      # for all

def randomvalue():
 if len(data)!=0:
  conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
  mycursor=conn.cursor()
  if data[1]=='4':
   x=random.randint(1, 500)
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (x, 7))
   print"stuf club lora available, random value=%s"%x
  elif data[1]=='3':
   x=random.randint(1, 500)
   y=random.randint(1, 500)
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (x, 6))
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (y, 7))
   print"stuf club and children park lora available, random value=%s and %s"%(x,y)
  elif data[1]=='2':
   x=random.randint(1, 500)
   y=random.randint(1, 500)
   z=random.randint(1, 500)
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (x, 5))
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (y, 6))
   mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (z, 7))
   print"All lora available, random values=%s, %s and %s"%(x,y,z)
  conn.commit()
  conn.close()
  mycursor.close()
 else:
  return
 return




while(1):                             
 randomvalue()
time.sleep(1)
