import time
import mysql.connector
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
def Average(lst):
 return sum(lst) / len(lst)
while (1):
 
 client = ModbusClient(method='rtu', port='COM1', stopbits=1, timeout=0.5, bytesize=8, parity='N', baudrate='9600')
 connection=client.connect()
 #print(connection)
 value=client.read_holding_registers(0,15,unit=1)
 cylinder = (value.registers[0],value.registers[1],value.registers[2],value.registers[3],value.registers[4],value.registers[5])
 y=Average (cylinder)
 conn = mysql.connector.connect(user='root', password='123456', host ='localhost', database='scanner')
 mycursor = conn.cursor()
 #print(value)
 #print(value.registers[0])
 
 mycursor.execute("update temperature2 set t1 = '%s',t2 = '%s',t3 = '%s',t4 = '%s',t5 = '%s',t6 = '%s',t7 = '%s', t8 = '%s', t9 = '%s',t10 = '%s',t11 = '%s',t12 = '%s',t13 = '%s', t14 = '%s', t15 = '%s', avg ='%s' where id =1" %(value.registers[0]/10,value.registers[1]/10, value.registers[2]/10, value.registers[3]/10, value.registers[4]/10,value.registers[5]/10,value.registers[6]/10,value.registers[7]/10,value.registers[8]/10,value.registers[9]/10,value.registers[10]/10,value.registers[11]/10,value.registers[12]/10, value.registers[13]/10, value.registers[14]/10,y/10))
 print(Average (cylinder))
  
 
 conn.commit()
 conn.close()
 mycursor.close()
 client.close()
 #conn.commit()
 
 time.sleep(0.5)
