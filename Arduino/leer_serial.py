
import serial
import time


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0)


while True:
    
    data = arduino.read(2)
    print(data)
    time.sleep(0.01)