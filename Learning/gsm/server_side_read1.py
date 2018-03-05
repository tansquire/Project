#!/usr/bin/python
import serial
import time
import mysql.connector
from time import gmtime, strftime
from datetime import datetime
ser = serial.Serial('/dev/ttyACM0', baudrate = 9600)
time.sleep(1)
start = time.time()


def scada():
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("select * FROM command") 
 list=mycursor.fetchall()
 #print list
 remote=int(list[2][2])
 opd=int(list[3][2])
 cld=int(list[4][2])
 if(opd and not cld):
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('OPENED', 8))
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('1', 9))
 elif(cld and not opd):
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('CLOSED', 8))
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('0', 9))
 elif(not cld and not opd):
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('INTERMEDIATE', 8)) 
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('2', 9))
 else:
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('PROBLEM', 8)) 
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('3', 9))
 if(remote):
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('REMOTE', 7))
 else:
  mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % ('LOCAL', 7))
 conn.commit()
 conn.close()
 mycursor.close()
 time.sleep(1)
 return

while(1):
 scada()
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("select * FROM GSMAI") 
 list=mycursor.fetchall()
 count_rcvd_from_A=int (list[4][2])
 count_rcvd_from_B=int (list[5][2])
 count_rcvd_from_C=int (list[15][2])
 count_rcvd_from_D=int (list[16][2])
 count_rcvd_from_Actuator=int (list[17][2])
 #count_sent_by_server=int (list[9][2])

 if(ser.inWaiting()>0):
  data=ser.readline()
  print(data)
  if('SMS No' in data and 'device' in data and '<' in data and '>' in data):
   data1=data.decode().split('\r\n')
   print(data1[0])
   
   if('actuator' in data1[0]):
    remote=int(data1[0][19])-6
    opd=int(data1[0][20])-6
    cld=int(data1[0][21])-6
    mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % (remote, 3))
    mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % (opd, 4))
    mycursor.execute("UPDATE command SET value='%s'WHERE id='%s'" % (cld, 5))
    print"Remote, opd, and cld status are=%s, %s and %s"%(remote, opd, cld)
    count_rcvd_from_Actuator=count_rcvd_from_Actuator+1
    mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (count_rcvd_from_Actuator, 18))  
    mycursor.execute("insert into gsm_test (id, name, value) values (%d, '%s', '%s')" % (1, datetime.now(),"Nos of valid message found from actuator=%d"%(count_rcvd_from_Actuator)))
   
   if('deviceA' in data1[0]):
    deviceA_data=data1[0][data1[0].find('<')+1:data1[0].find('>')]
    print(deviceA_data)
    print"lakewell data=%s"%(deviceA_data)
    mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (deviceA_data, 1))
    count_rcvd_from_A=count_rcvd_from_A+1
    mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (count_rcvd_from_A, 5))  
    mycursor.execute("insert into gsm_test (id, name, value) values (%d, '%s', '%s')" % (1, datetime.now(),"Nos of valid message found from deviceA=%d"%(count_rcvd_from_A)))

   if('deviceB' in data1[0]):
    deviceB_data=data1[0][data1[0].find('<')+1:data1[0].find('>')]
    print(deviceB_data)
    print"children park data=%s"%(deviceB_data)
    mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (deviceB_data, 2))
    count_rcvd_from_B=count_rcvd_from_B+1
    mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (count_rcvd_from_B, 6))  
    mycursor.execute("insert into gsm_test (id, name, value) values (%d, '%s', '%s')" % (1, datetime.now(),"Nos of valid message found from deviceB=%d"%(count_rcvd_from_B)))
   
   if('deviceC' in data1[0]):
    deviceC_data=data1[0][data1[0].find('<')+1:data1[0].find('>')]
    print(deviceC_data)
    print"stuff club data=%s"%(deviceC_data)
    mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (deviceC_data, 3))
    count_rcvd_from_C=count_rcvd_from_C+1
    mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (count_rcvd_from_C, 16))  
    mycursor.execute("insert into gsm_test (id, name, value) values (%d, '%s', '%s')" % (1, datetime.now(),"Nos of valid message found from deviceC=%d"%(count_rcvd_from_C)))
   
   if('deviceD' in data1[0]):
    deviceD_data=data1[0][data1[0].find('<')+1:data1[0].find('>')]
    print(deviceD_data)
    print"RR sump data=%s"%(deviceD_data)
    mycursor.execute("UPDATE AI SET value='%s'WHERE id='%s'" % (deviceD_data, 4))
    count_rcvd_from_D=count_rcvd_from_D+1
    mycursor.execute("UPDATE GSMAI SET value='%s'WHERE id='%s'" % (count_rcvd_from_D, 17))  
    mycursor.execute("insert into gsm_test (id, name, value) values (%d, '%s', '%s')" % (1, datetime.now(),"Nos of valid message found from deviceD=%d"%(count_rcvd_from_D)))
 
 conn.commit()
 conn.close()
 mycursor.close() 
 time.sleep(.1)
 
