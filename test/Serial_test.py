import serial
import time

ser = serial.Serial("com1", 115200, timeout=0.5)

if ser.isOpen():
    ser.close()
ser.open()

while 1:
    success_bytes = ser.write(b'\nThis is data for test')
    time.sleep(2)
    print(success_bytes)