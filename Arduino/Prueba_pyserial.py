import serial
import matplotlib.pyplot as plt
import time


arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
point = 0
fig, ax = plt.subplots()
plt.ion()

maxlen = 20
x = []
y = []

while True:
    
    data = arduino.read(1).decode()
    print(data)
    
    time.sleep(0.01)
    if data:
        data = int(data)
        x.append(point)
        y.append(data)
        if len(x) > maxlen:
            x = x[1:]
            y = y[1:]
        plt.plot(x, y, color='r')
        point += 1
        plt.pause(0.02)

        ax.clear()
        #plt.ylim([0, 1023])
        plt.show()