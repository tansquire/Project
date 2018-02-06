#!/usr/bin/python
import mysql.connector
import time
import pygame


def sound():
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("UPDATE DO SET value= '0' WHERE id=1")
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("SumpArea.wav")
 pygame.mixer.music.play()
 pygame.mixer.music.set_volume(0.3)
 time.sleep(8)
 pygame.mixer.music.stop()
 
 
 conn.commit()
 conn.close()
 mycursor.close()
 return




time.sleep(3)
while(1):

 time.sleep(2)
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute('select * FROM DO where id=1') 
 list=mycursor.fetchall()
 print("command values are")
 print(list[0][2])
 if(list[0][2]=='1'):
   sound()
 conn.close()
 mycursor.close()
  
 
