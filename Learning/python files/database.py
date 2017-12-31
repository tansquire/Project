#!/usr/bin/python


import mysql.connector
import time
conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='test')
mycursor=conn.cursor()

def getdata(y):
 return y
print("importing to database..")
x=1 
while(x<20):
 x=x+1
 print(x)
 time.sleep(1)

 data=getdata(x)
#while 1:
 mycursor.execute("UPDATE student SET roll= %s WHERE idstudent=10" %(data))
 conn.commit()


 

