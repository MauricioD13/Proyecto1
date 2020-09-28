import matplotlib.pyplot as plt
import numpy as np
import sys


def guardar(archivo,time,voltage):
      for line in archivo0:
        
        linea=line.split(",")
        time.append(float(linea[0]+"."+linea[1]))
        voltage.append(float(linea[2]+"."+linea[3]))  


archivo0=open("./datos/primera_etapa_entrada_diferencial_1mV.txt","r");
archivo1=open("./datos/primera_etapa_filtro_1mV.txt","r");
archivo2=open("./datos/segunda_etapa_filtro_1mV.txt","r");
#~/Documents/Python/Proyecto/
#parameter=sys.argv[1].split(".")

#file_write=open(parameter[0]+"_fixed.txt","w")
labels=archivo0.readline().split(",")
labels[1]=labels[1].replace("\n","")
print(labels)
print("-------------")
time0=[] 
voltage0=[]
time1=[] 
voltage1=[]
time2=[] 
voltage2=[]

guardar(archivo0,time0,voltage0)
guardar(archivo1,time1,voltage1)
guardar(archivo2,time2,voltage2)
        #file_write.write(linea[0]+"."+linea[1]+" "+linea[2]+"."+linea[3])
archivo0.close()
#file_write.close()
a=np.array(time0[1000:5000])
b=np.array(voltage0[1000:5000])

fig, ax=plt.subplots()


print("MUESTRAS:",len(time0))
ax.plot(a,b)  # Plot some data on the axes.
plt.grid(True,)

ax.set_ylabel(labels[1])
ax.set_xlabel(labels[0])
plt.show()
                    
