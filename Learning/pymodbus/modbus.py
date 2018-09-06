import time
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadHoldingRegistersResponse
while (1):
 client = ModbusClient(method='rtu', port='COM1', stopbits=1, timeout=0.5, bytesize=8, parity='N', baudrate='9600')
 connection=client.connect()
 #print(connection)
 value=client.read_holding_registers(0,15,unit=1)
 print(value.registers)
 client.close()
 time.sleep(0.5)
