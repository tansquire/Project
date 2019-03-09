#!/usr/bin/python
import mysql.connector
import time
import pygame
import random
dub_dg_new=dub_mlmovopd_new=dub_mlmovcld_new=dub_llmovopd_new=dub_llmovcld_new=dub_door_new=dub_fire_new=dub_dg_old=dub_mlmovopd_old=dub_mlmovcld_old=dub_llmovopd_old=dub_llmovcld_old=dub_door_old=dub_fire_old=0
ktp_dg_new=ktp_mlmovopd_new=ktp_mlmovcld_new=ktp_llmovopd_new=ktp_llmovcld_new=ktp_door_new=ktp_fire_new=ktp_dg_old=ktp_mlmovopd_old=ktp_mlmovcld_old=ktp_llmovopd_old=ktp_llmovcld_old=ktp_door_old=ktp_fire_old=0
r_dg_new=r_mlmovopd_new=r_mlmovcld_new=r_llmovopd_new=r_llmovcld_new=r_door_new=r_fire_new=r_dg_old=r_mlmovopd_old=r_mlmovcld_old=r_llmovopd_old=r_llmovcld_old=r_door_old=r_fire_old=0
g_dg_new=g_mlmovopd_new=g_mlmovcld_new=g_llmovopd_new=g_llmovcld_new=g_door_new=g_fire_new=g_dg_old=g_mlmovopd_old=g_mlmovcld_old=g_llmovopd_old=g_llmovcld_old=g_door_old=g_fire_old=0

def hooter(s):
 pygame.init()
 pygame.mixer.init()
 pygame.mixer.music.load(s)
 pygame.mixer.music.play()
 time.sleep(8)
 pygame.mixer.music.stop()
 return

while(1):
 try:
  conn=mysql.connector.connect(user='root',password='123456',host='192.168.100.10',database='rtu')
  mycursor=conn.cursor()
  mycursor.execute("select * FROM rcp") 
  list=mycursor.fetchall()
  #print list[3]
  print("It is working")
  dub_dg_new=int(list[0][1])
  dub_mlmovopd_new=int(list[0][2])
  dub_mlmovcld_new=int(list[0][3])
  dub_llmovopd_new=int(list[0][4])
  dub_llmovcld_new=int(list[0][5])
  dub_door_new=int(list[0][6])
  dub_fire_new=int(list[0][7])


  ktp_dg_new=int(list[3][1])
  ktp_mlmovopd_new=int(list[3][2])
  ktp_mlmovcld_new=int(list[3][3])
  ktp_llmovopd_new=int(list[3][4])
  ktp_llmovcld_new=int(list[3][5])
  ktp_door_new=int(list[3][8])
  ktp_fire_new=int(list[3][6])


  r_dg_new=int(list[1][1])
  r_mlmovopd_new=int(list[1][2])
  r_mlmovcld_new=int(list[1][3])
  r_llmovopd_new=int(list[1][4])
  r_llmovcld_new=int(list[1][5])
  r_door_new=int(list[1][8])
  r_fire_new=int(list[1][6])


  g_dg_new=int(list[2][1])
  g_mlmovopd_new=int(list[2][2])
  g_mlmovcld_new=int(list[2][3])
  g_llmovopd_new=int(list[2][4])
  g_llmovcld_new=int(list[2][5])
  g_door_new=int(list[2][8])
  g_fire_new=int(list[2][6])


  
  if(dub_dg_new-dub_dg_old==1):
   print("DG started at Dubrajpur RCP")
   hooter("dg_start.wav")
  if(dub_dg_new-dub_dg_old==-1):
   print("DG stopped at Dubrajpur RCP")
   hooter("dg_stop.wav")
  if(dub_mlmovopd_new-dub_mlmovopd_old==1):
   print("ML MOV opened at Dubrajpur RCP")
   hooter("hooter.wav")
  if(dub_mlmovcld_new-dub_mlmovcld_old==1):
   print("ML MOV closed at Dubrajpur RCP")
   hooter("hooter.wav")
  if(dub_llmovopd_new-dub_llmovopd_old==1):
   print("LL MOV opened at Dubrajpur RCP")
   hooter("hooter.wav")
  if(dub_llmovcld_new-dub_llmovcld_old==1):
   print("LL MOV closed at Dubrajpur RCP")
   hooter("hooter.wav")
  if(dub_door_new-dub_door_old==-1):
   print("Door open at Dubrajpur RCP")
   hooter("INTRUSION.wav")
  if(dub_fire_new-dub_fire_old==1):
   print("Fire detected at Dubrajpur RCP")
   hooter("FIRE.wav")

  if(ktp_dg_new-ktp_dg_old==1):
   print("DG started at Kantapukur RCP")
   hooter("dg_start_ktp.wav")
  if(ktp_dg_new-ktp_dg_old==-1):
   print("DG stopped at Kantapukur RCP")
   hooter("dg_stop_ktp.wav")
  if(ktp_mlmovopd_new-ktp_mlmovopd_old==1):
   print("ML MOV opened at Kantapukur RCP")
   hooter("hooter.wav")
  if(ktp_mlmovcld_new-ktp_mlmovcld_old==1):
   print("ML MOV closed at Kantapukur RCP")
   hooter("hooter.wav")
  if(ktp_llmovopd_new-ktp_llmovopd_old==1):
   print("LL MOV opened at Kantapukur RCP")
   hooter("hooter.wav")
  if(ktp_llmovcld_new-ktp_llmovcld_old==1):
   print("LL MOV closed at Kantapukur RCP")
   hooter("hooter.wav")
  if(ktp_door_new-ktp_door_old==-1):
   print("Door open at Kantapukur RCP")
   hooter("intrusion_ktp.wav")
  if(ktp_fire_new-ktp_fire_old==1):
   print("Fire detected at Kantapukur RCP")
   hooter("fire_ktp.wav")


  if(r_dg_new-r_dg_old==1):
   print("DG started at Rakh RCP")
   hooter("Rakh-start.wav")
  if(r_dg_new-r_dg_old==-1):
   print("DG stopped at Rakh RCP")
   hooter("Rakh-stop.wav")
  if(r_mlmovopd_new-r_mlmovopd_old==1):
   print("ML MOV opened at Rakh RCP")
   hooter("hooter.wav")
  if(r_mlmovcld_new-r_mlmovcld_old==1):
   print("ML MOV closed at Rakh RCP")
   hooter("hooter.wav")
  if(r_llmovopd_new-r_llmovopd_old==1):
   print("LL MOV opened at Rakh RCP")
   hooter("hooter.wav")
  if(r_llmovcld_new-r_llmovcld_old==1):
   print("LL MOV closed at Rakh RCP")
   hooter("hooter.wav")
  if(r_door_new-r_door_old==-1):
   print("Door open at Rakh RCP")
   hooter("Rakh-intrusion.wav")
  if(r_fire_new-r_fire_old==1):
   print("Fire detected at Rakh RCP")
   hooter("hooter.wav")

  if(g_dg_new-g_dg_old==-1):
   print("DG started at Gopibadh RCP")
   hooter("Gopi-start.wav")
  if(g_dg_new-g_dg_old==1):
   print("DG stopped at Gopibadh RCP")
   hooter("Gopi-stop.wav")
  if(g_mlmovopd_new-g_mlmovopd_old==1):
   print("ML MOV opened at Gopibadh RCP")
   hooter("hooter.wav")
  if(g_mlmovcld_new-g_mlmovcld_old==1):
   print("ML MOV closed at Gopibadh RCP")
   hooter("hooter.wav")
  if(g_llmovopd_new-g_llmovopd_old==1):
   print("LL MOV opened at Gopibadh RCP")
   hooter("hooter.wav")
  if(g_llmovcld_new-g_llmovcld_old==1):
   print("LL MOV closed at Gopibadh RCP")
   hooter("hooter.wav")
  if(g_door_new-g_door_old==-1):
   print("Door open at Gopibadh RCP")
   hooter("Gopi-intrusion.wav")
  if(g_fire_new-g_fire_old==1):
   print("Fire detected at Gopibadh RCP")
   hooter("hooter.wav")
   
   
  dub_dg_old=dub_dg_new
  dub_mlmovopd_old=dub_mlmovopd_new
  dub_mlmovcld_old=dub_mlmovcld_new
  dub_llmovopd_old=dub_llmovopd_new
  dub_llmovcld_old=dub_llmovcld_new
  dub_door_old=dub_door_new
  dub_fire_old=dub_fire_new


  ktp_dg_old=ktp_dg_new
  ktp_mlmovopd_old=ktp_mlmovopd_new
  ktp_mlmovcld_old=ktp_mlmovcld_new
  ktp_llmovopd_old=ktp_llmovopd_new
  ktp_llmovcld_old=ktp_llmovcld_new
  ktp_door_old=ktp_door_new
  ktp_fire_old=ktp_fire_new

  r_dg_old=r_dg_new
  r_mlmovopd_old=r_mlmovopd_new
  r_mlmovcld_old=r_mlmovcld_new
  r_llmovopd_old=r_llmovopd_new
  r_llmovcld_old=r_llmovcld_new
  r_door_old=r_door_new
  r_fire_old=r_fire_new


  g_dg_old=g_dg_new
  g_mlmovopd_old=g_mlmovopd_new
  g_mlmovcld_old=g_mlmovcld_new
  g_llmovopd_old=g_llmovopd_new
  g_llmovcld_old=g_llmovcld_new
  g_door_old=g_door_new
  g_fire_old=g_fire_new

  conn.commit()
  conn.close()
  mycursor.close()
  time.sleep(1)
 except:
  print("error") 
