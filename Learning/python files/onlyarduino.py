#!/usr/bin/python
import serial
import time
import mysql.connector
import serial.tools.list_ports
#x=serial.tools.list_ports.comports()
#for i in range(0,len(x)):
 #if('USB' in x[i][0]):
  #y=x[i][0]
  #print(y)

#ser = serial.Serial(y, baudrate = 9600, timeout = 1)
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)

def getvalue():
 ser.write(b'g')
 data=ser.readline().decode('ascii')
 data=str(data)
 return data

def opened():
 ser.write(b'c')
 data=ser.readline()
 print ("opened= %s" % data)
 if len(data) != 0:
   if(int(data[0])==7):
    return ('1')
   else:
    return ('0')
 else:
  print('please wait')

def remote():
 ser.write(b'd')
 data=ser.readline()
 print ("remote= %s" % data)
 if len(data) != 0:
   if(int(data[0])==7):
    return ('1')
   else:
    return ('0')
 else:
  print('please wait')


def closed():
 ser.write(b'e')
 data=ser.readline()
 print ("closed= %s" % data)
 if len(data) != 0:
   if(int(data[0])==7):
    return ('1')
   else:
    return ('0')
 else:
  print('please wait')


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




conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
mycursor=conn.cursor()
mycursor.execute("UPDATE command SET open= '0' WHERE valve=1")
mycursor.execute("UPDATE command SET close= '0' WHERE valve=1")
conn.commit()
conn.close()
mycursor.close()



time.sleep(3)
while(1):
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
 mycursor=conn.cursor()
 mycursor.execute('select * FROM command') 
 list=mycursor.fetchall()
 print "open=%s, close=%s" % (list[0][1], list[0][2])
 #print(list[0][2])
 #print(list[0][1])
 
 time.sleep(2)
 if(list[0][1]=='1'):
  open()
 if(list[0][2]=='1'):
   close()

 mycursor.execute("UPDATE command SET opened= '%s' WHERE valve=1" %(opened()))
 mycursor.execute("UPDATE command SET closed= '%s' WHERE valve=1" %(closed()))
 #mycursor.execute("UPDATE command SET remote= '%s' WHERE valve=1" %(remote()))
 mycursor.execute("UPDATE command SET remote= '1' WHERE valve=1")
 conn.commit()
 conn.close()
 mycursor.close()
 time.sleep(1)


