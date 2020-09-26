import matplotlib.pyplot as plt
import numpy as np
import sys
archivo=open(sys.argv[1],"r");
print(sys.argv[1])
parameter=sys.argv[1].split(".")

file_write=open(parameter[0]+"_fixed.txt","w")
print(archivo.readline())


print("-------------")
time=[] 
voltage=[]
for line in archivo:
    
    linea=line.split(",")
    time.append(float(linea[0]+"."+linea[1]))
    voltage.append(float(linea[2]+"."+linea[3]))
    file_write.write(linea[0]+"."+linea[1]+" "+linea[2]+"."+linea[3])
archivo.close()
file_write.close()
print(len(time))
a=np.array(time[1000:10000:10])
b=np.array(voltage[1000:10000:10])


fig, ax=plt.subplots()
ax.plot(a,b)  # Plot some data on the axes.
#plt.axis("off")
ax.set_ylabel('voltaje')
ax.set_xlabel('tiempo')
plt.show()


