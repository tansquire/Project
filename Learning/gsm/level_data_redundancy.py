#!/usr/bin/python
import serial
import time
import mysql.connector

lake_well_lora_data=childrenpark_lora_data=stuff_club_lora_data=lake_well_gsm_data=childrenpark_gsm_data=stuff_club_gsm_data='0'
lake_well_final_data=childrenpark_final_data=stuff_club_final_data='0'
while(1):
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 mycursor.execute("select * FROM DI where id=3") 
 list=mycursor.fetchall()
 lake_well_lora_status=(list[0][2])
 mycursor.execute("select * FROM DI where id=4") 
 list=mycursor.fetchall()
 childrenpark_lora_status=(list[0][2])
 mycursor.execute("select * FROM DI where id=5") 
 list=mycursor.fetchall()
 stuff_club_lora_status=(list[0][2])
 print"lakewell, children, and stuff_club comm availabilities respectively are=%s, %s and %s"%(lake_well_lora_status,childrenpark_lora_status,stuff_club_lora_status)
 mycursor.execute("select * FROM AI where id=1") 
 list=mycursor.fetchall()
 lake_well_lora_data=(list[0][2])
 mycursor.execute("select * FROM AI where id=2") 
 list=mycursor.fetchall()
 childrenpark_lora_data=(list[0][2])
 mycursor.execute("select * FROM AI where id=3") 
 list=mycursor.fetchall()
 stuff_club_lora_data=(list[0][2])
 print"lakewell, children, and stuff_club lora data respectively are=%s, %s and %s"%(lake_well_lora_data,childrenpark_lora_data,stuff_club_lora_data)
 mycursor.execute("select * FROM GSMAI where id=1") 
 list=mycursor.fetchall()
 lake_well_gsm_data=(list[0][2])
 mycursor.execute("select * FROM GSMAI where id=2") 
 list=mycursor.fetchall()
 childrenpark_gsm_data=(list[0][2])
 mycursor.execute("select * FROM GSMAI where id=3") 
 list=mycursor.fetchall()
 stuff_club_gsm_data=(list[0][2])
 print"lakewell, children, and stuff_club gsm data respectively are=%s, %s and %s"%(lake_well_gsm_data,childrenpark_gsm_data,stuff_club_gsm_data)

 if(lake_well_lora_status=='1'):
  lake_well_final_data=lake_well_lora_data
 else:
  lake_well_final_data=lake_well_gsm_data

 if(childrenpark_lora_status=='1'):
  childrenpark_final_data=childrenpark_lora_data
 else:
  childrenpark_final_data=childrenpark_gsm_data

 if(stuff_club_lora_status=='1'):
  stuff_club_final_data=stuff_club_lora_data
 else:
  stuff_club_final_data=stuff_club_gsm_data

 mycursor.execute("UPDATE AIFINAL SET value='%s'WHERE id='%s'" % (lake_well_final_data, 1))
 mycursor.execute("UPDATE AIFINAL SET value='%s'WHERE id='%s'" % (childrenpark_final_data, 2))
 mycursor.execute("UPDATE AIFINAL SET value='%s'WHERE id='%s'" % (stuff_club_final_data, 3))
 conn.commit()
 print"lakewell, children, and stuff_club final data respectively are=%s, %s and %s"%(lake_well_final_data,childrenpark_final_data,stuff_club_final_data)
 conn.close()
 mycursor.close()
 time.sleep(5)



