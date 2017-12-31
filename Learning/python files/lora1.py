#!/usr/bin/python
import serial
import time
import mysql.connector

#import serial.tools.list_ports
#x=serial.tools.list_ports.comports()
#for i in range(0,len(x)):
 #if('USB' in x[i][0]):
  #y=x[i][0]
  #print(y)
#ser = serial.Serial(y, baudrate = 9600, timeout = 5)

ser = serial.Serial('/dev/ttyUSB0', baudrate = 9600, timeout = 1)




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


###################  initial reset  ########################################

conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
mycursor=conn.cursor()
mycursor.execute("UPDATE command SET open= '0' WHERE valve=1")
mycursor.execute("UPDATE command SET close= '0' WHERE valve=1")
conn.commit()
conn.close()
mycursor.close()


##############################################################################


time.sleep(3)
while(1):
 
 ##############################command#############################
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
#####################################################################

 data=ser.readline().decode().split('\r\n')
 if len(data[0]) != 0:
  print("Received data")
  print(data)
  print(data[0][0])
  print(data[0][1])
  print(data[0][2])
  if(int(data[0][0])==7):
   lr=1
  else:
   lr=0
  if(int(data[0][1])==7):
   opd=1
  else:
   opd=0
  if(int(data[0][2])==7):
   cld=1
  else:
   cld=0
  print("Actual status")
  print(lr)
  print(opd)
  print(cld)
 
 #print("Remote, open, close status respectively are")
 #print(opd)
 #print("cld=%s" % cld)
 #print("lr=%s" % lr)
 
 #mycursor.execute("UPDATE command SET opened='%s', closed='%s' WHERE valve='%s'" % (opened(), closed(), 1))
 #mycursor.execute("UPDATE command SET opened='%s', closed='%s', remote='%s' WHERE valve='%s'" % (opd, cld, lr, 1))
  mycursor.execute("UPDATE command SET opened='%s', closed='%s', remote='%s' WHERE valve='%s'" % (opd, cld, 1, 1))
 #mycursor.execute("UPDATE command SET closed= %s WHERE valve=1" %(closed()))
 #mycursor.execute("UPDATE command SET remote= %s WHERE valve=1" %(remote()))
 #mycursor.execute("UPDATE command SET remote= '1' WHERE valve=1")
 #mycursor.execute("UPDATE command SET opened= '0' WHERE valve=1")
  conn.commit()
  conn.close()
  mycursor.close()
  


 else:
  print('Please wait..')
 
 time.sleep(1)












