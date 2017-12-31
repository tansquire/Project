#!/usr/bin/python
import serial
import time
import mysql.connector

ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600, timeout = 1)

def getvalue():
 ser.write(b'g')
 time.sleep(1)
 data=ser.readline().decode('ascii')
 
 return data

def opened():
 ser.write(b'c')
 #time.sleep(8)
 data=ser.readline()
 
 if(data==0 or data==1):
  data1=data
 print("opd=%s" % data1)
 return data1

def remote():
 ser.write(b'd')
 #time.sleep(1)
 data=ser.readline()
 print("remote=%s" % data)
 return data

def closed():
 ser.write(b'e')
 #time.sleep(1)
 data=ser.readline()
 print("cld=%s" % data)
 return data



def open():
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
 mycursor=conn.cursor()
 ser.write(b'a')
 mycursor.execute("UPDATE command SET open= '0' WHERE valve=1")
 conn.commit()
 conn.close()
 mycursor.close()
 return

def close():
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
 mycursor=conn.cursor()
 ser.write(b'b')
 mycursor.execute("UPDATE command SET close= '0' WHERE valve=1")
 conn.commit()
 conn.close()
 mycursor.close()
 return


while(1):
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
 mycursor=conn.cursor()
 mycursor.execute('select * FROM command') 
 list=mycursor.fetchall()
 print("command values are")
 print(list[0][2])
 print(list[0][1])
 
 
 #time.sleep(2)
 if(list[0][1]=='1'):
  open()
 if(list[0][2]=='1'):
   close()
 
 opd=opened()
 cld=closed()
 lr=remote()
 
 #print("Remote, open, close status respectively are")
 #print(opd)
 #print("cld=%s" % cld)
 #print("lr=%s" % lr)
 
 #mycursor.execute("UPDATE command SET opened='%s', closed='%s' WHERE valve='%s'" % (opened(), closed(), 1))
 mycursor.execute("UPDATE command SET opened='%s', closed='%s', remote='%s' WHERE valve='%s'" % (opd, cld, lr, 1))
 #mycursor.execute("UPDATE command SET closed= %s WHERE valve=1" %(closed()))
 #mycursor.execute("UPDATE command SET remote= %s WHERE valve=1" %(remote()))
 #mycursor.execute("UPDATE command SET remote= '1' WHERE valve=1")
 #mycursor.execute("UPDATE command SET opened= '0' WHERE valve=1")
 conn.commit()
 conn.close()
 mycursor.close()
 time.sleep(1)


