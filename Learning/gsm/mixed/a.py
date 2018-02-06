#!/usr/bin/python
import os
import subprocess, platform
import time
import mysql.connector

def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)

    except Exception, e:
        return 0

    return 1

time.sleep(1)
while(1):
 conn=mysql.connector.connect(user='root',password='gowsalya',host='10.21.160.201',database='scada')
 mycursor=conn.cursor()
 pingstatus = pingOk("10.22.54.85")
 print pingstatus
 mycursor.execute("UPDATE DI SET value='%s'WHERE id='%s'" % (pingstatus, 2))
 conn.commit()
 conn.close()
 mycursor.close()
 time.sleep(1)



























while(1):
 time.sleep(1)
 
