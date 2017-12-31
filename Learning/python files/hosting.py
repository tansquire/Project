#!/usr/bin/python


import time
import mysql.connector
y=2

conn=mysql.connector.connect(user='waterci2_dadu',password='9836373993',host='103.53.42.63',database='waterci2_test')
mycursor=conn.cursor()
conn1=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
mycursor1=conn1.cursor()


mycursor1.execute("UPDATE level SET Value= %s WHERE Device=1" %(y))
conn.commit()

mycursor1.execute("SELECT * FROM level");
list=mycursor1.fetchall()
x=list[0][2]



print('importing data to database..')
while 1:
 mycursor.execute("UPDATE level SET Value= %s WHERE Device=1" %(x))
 conn.commit()
 print(x)
 time.sleep(2)
 
 
 
