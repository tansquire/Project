#!/usr/bin/python
import serial
import time
import paramiko
from datetime import datetime
from datetime import date
while(1):
 try:
  ser = serial.Serial('/dev/ttyACM0', baudrate = 9600)
  data=ser.readline().decode().split('\r\n')
  x=str(data)
  if(('Tag' in x) and len(data[0])==23):
   now = datetime.now()
   today = date.today()
   time1 = now.strftime("%H:%M:%S")
   date1 = today.strftime("%d/%m/%Y")
   print ("Getting data ...")
   #print data[0][-8:]
   send_data=date1+'p'+data[0][-8:]+'q'+time1
   print send_data
   #print date1
   #print time1
   ssh = paramiko.SSHClient()
   ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh.connect('HOST_IP', username='dadu', password='PASSWORD', key_filename='/home/pi/.ssh/id_rsa')
   ftp = ssh.open_sftp()
   file=ftp.file('/home/dadu/partha.txt', "w", -1)
   file.write(send_data)
   file.flush()
   ftp.close()
   ssh.close()
   print("data updated in the server")
  #time.sleep(0.01)
 except:
  print("error")
 time.sleep(0.01)
