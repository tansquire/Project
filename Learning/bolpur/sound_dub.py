#!/usr/bin/python
import mysql.connector
import time
import pygame
import random
dub_dg_new=dub_mlmovopd_new=dub_mlmovcld_new=dub_llmovopd_new=dub_llmovcld_new=dub_door_new=dub_fire_new=dub_dg_old=dub_mlmovopd_old=dub_mlmovcld_old=dub_llmovopd_old=dub_llmovcld_old=dub_door_old=dub_fire_old=0
def dg_start():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("dg_start.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def dg_stop():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("dg_stop.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def ml_opd():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("MLOPD.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def ml_cld():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("MLCLD.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def ll_opd():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("LLOPD.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def ll_cld():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("LLCLD.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def door():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("INTRUSION.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return
def fire():
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load("FIRE.wav")
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return

while(1):
  conn=mysql.connector.connect(user='root',password='123456',host='192.168.100.10',database='rtu')
  mycursor=conn.cursor()
  mycursor.execute("select * FROM rcp") 
  list=mycursor.fetchall()
  print list[3]
  dub_dg_new=int(list[0][1])
  dub_mlmovopd_new=int(list[0][2])
  dub_mlmovcld_new=int(list[0][3])
  dub_llmovopd_new=int(list[0][4])
  dub_llmovcld_new=int(list[0][5])
  dub_door_new=int(list[0][6])
  dub_fire_new=int(list[0][7])
  if(dub_dg_new-dub_dg_old==1):
   print("DG started at Dubrajpur RCP")
   dg_start()
  if(dub_dg_new-dub_dg_old==-1):
   print("DG stopped at Dubrajpur RCP")
   dg_stop()
  if(dub_mlmovopd_new-dub_mlmovopd_old==1):
   print("ML MOV opened at Dubrajpur RCP")
   ml_opd()
  if(dub_mlmovcld_new-dub_mlmovcld_old==1):
   print("ML MOV closed at Dubrajpur RCP")
   ml_cld()
  if(dub_llmovopd_new-dub_llmovopd_old==1):
   print("LL MOV opened at Dubrajpur RCP")
   ll_opd()
  if(dub_llmovcld_new-dub_llmovcld_old==1):
   print("LL MOV closed at Dubrajpur RCP")
   ll_cld()
  if(dub_door_new-dub_door_old==-1):
   print("Door open at Dubrajpur RCP")
   door()
  if(dub_fire_new-dub_fire_old==1):
   print("Fire detected at Dubrajpur RCP")
   fire()
   
  dub_dg_old=dub_dg_new
  dub_mlmovopd_old=dub_mlmovopd_new
  dub_mlmovcld_old=dub_mlmovcld_new
  dub_llmovopd_old=dub_llmovopd_new
  dub_llmovcld_old=dub_llmovcld_new
  dub_door_old=dub_door_new
  dub_fire_old=dub_fire_new
  conn.commit()
  conn.close()
  mycursor.close()
  time.sleep(1)  
