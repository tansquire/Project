#!/usr/bin/python
import time
i=0
while(i<10):
 f=open('file.txt','w')
 f.write(str(i))
 f.close()
 time.sleep(3)
 i=i+1
print('ok')


