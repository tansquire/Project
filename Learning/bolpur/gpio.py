import RPi.GPIO as GPIO
import time
cylinder_high=5
cylinder_dev=6
gearbox_high=13
pump_de_high=19
pump_nde_high=26
sensor_fault=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(cylinder_high, GPIO.OUT)
GPIO.setup(cylinder_dev, GPIO.OUT)
GPIO.setup(gearbox_high, GPIO.OUT)
GPIO.setup(pump_de_high, GPIO.OUT)
GPIO.setup(pump_nde_high, GPIO.OUT)
GPIO.setup(sensor_fault, GPIO.OUT)

while(1):
 GPIO.output(cylinder_high, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(cylinder_dev, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(gearbox_high, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(pump_de_high, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(pump_nde_high, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(sensor_fault, GPIO.HIGH)
 time.sleep(2)
 GPIO.output(cylinder_high, GPIO.LOW)
 time.sleep(2)
 GPIO.output(cylinder_dev, GPIO.LOW)
 time.sleep(2)
 GPIO.output(gearbox_high, GPIO.LOW)
 time.sleep(2)
 GPIO.output(pump_de_high, GPIO.LOW)
 time.sleep(2)
 GPIO.output(pump_nde_high, GPIO.LOW)
 time.sleep(2)
 GPIO.output(sensor_fault, GPIO.LOW)
 time.sleep(5)