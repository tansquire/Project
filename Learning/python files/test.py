#!/usr/bin/python
import time



i=0;
while 1:
 lr=0
 cld=0
 opd=0
 #data=[u'667666']
 data=[u'']
 if len(data) != 0:
  print("Data length")
  print (len(data))
  i=i+1
  print("Total nos data received ")
  print(i)
  print("raw data received")
  print(data)
  print("Data after filtering")
  print(data[0])
 
  if (int(data[0][0])==7):
   lr=1
  else:
   lr=0
  if (int(data[0][1])==7):
   opd=1
  else:
   opd=0
  if (int(data[0][2])==7):
   cld=1
  else:
   cld=0
  
  print("Bit by bit data")
  print(data[0][0])
  print(data[0][1])
  print(data[0][2])
 
  print("Actual status")
  print(lr)
  print(opd)
  print(cld)
  time.sleep(2)
 else:
  print("No data received")
