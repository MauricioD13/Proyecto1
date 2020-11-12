import matplotlib.pyplot as plt
import numpy as np
import mplcursors



def guardar(archivo,x,voltage0):
        labels=[]
        labels=archivo.readline().split(",")
        #labels[1]=labels[1].replace("\n","")
        i=0
        for line in archivo:
                linea=line.split(",")
                x.append(float(linea[0]))
                voltage0.append(float(linea[1]))
                
                i+=1
                if(i>=20000):
                        break  
        return labels
option=input("Opcion?: ")

if(option=="psrr"):
        archivo=open("./datos/PSRR_simulacion.csv","r");
        frequency=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]

        guardar(archivo,frequency,voltage0)
        frequency_array=np.array(frequency)
        voltage_array0=np.array(voltage0)
        fig, ax=plt.subplots()

        ax.plot(frequency_array,voltage_array0,'r',label="PSRR")  # Plot some data on the axes.
        ax.set_ylabel("Voltage")
        ax.set_xlabel("Frecuencia [Hz]")
        
        ax.set_xscale('log')

        ax.grid(True)
        
        
        
        plt.legend(loc='upper right')
        plt.show()