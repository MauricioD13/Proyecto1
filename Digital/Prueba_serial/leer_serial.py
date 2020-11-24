
import serial
import time


puerto = serial.Serial('COM5', 9600, timeout=1)

datos = []
while True:
    
    data = puerto.readline().decode()#.split("\r")[0]
    #datos = data.split("\t")
    print(data)
    time.sleep(0.01)