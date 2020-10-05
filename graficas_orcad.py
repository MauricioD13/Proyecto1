import matplotlib.pyplot as plt
import numpy as np
import mplcursors




def guardar(archivo,x,voltage0,voltage1,voltage2):
        labels=[]
        labels=archivo.readline().split(",")
        #labels[1]=labels[1].replace("\n","")
        i=0
        for line in archivo:
                linea=line.split(",")
                x.append(float(linea[0]))
                voltage0.append(float(linea[1]))
                voltage1.append(float(linea[2]))
                voltage2.append(float(linea[3]))
                
                i+=1
                if(i>=20000):
                        break  
        return labels
option=input("Opcion?: ")
if(option=="manejo"):
        archivo=open("./datos/ganancia_simulacion.csv","r");
        time=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]

        guardar(archivo,voltage0,voltage1,voltage2,time)

        print(voltage0[0:10])
        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        voltage_array2=np.array(voltage2)


        fig, ax=plt.subplots()
        ax.plot(voltage_array0,voltage_array1,label="Manejo") 
        plt.title("Manejo Simulacion")
        ax.set_xlabel("Voltaje entrada")
        ax.set_ylabel("Voltaje salida")
        mplcursors.cursor()
        plt.grid(True)
        plt.show()
if(option=="ganancia"):
        archivo=open("./datos/ganacia_simulacion.csv","r");
        frequency=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]

        guardar(archivo,frequency,voltage0,voltage1,voltage2)

        frequency_array=np.array(frequency)
        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        voltage_array2=np.array(voltage2)
        fig, ax=plt.subplots()

        ax.plot(frequency_array,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax.set_ylabel("Voltage")
        ax.set_xlabel("Frecuencia [Hz]")
        
        ax.set_xscale('log')
        ax.grid(True)
        ax.set(ylim=(0,1))
        
        ax.set_title("Ganancia simulacion V/V , Entrada 1mV")
        ax.plot(frequency_array,voltage_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        
        ax.plot(frequency_array,voltage_array2,label="Tercera Etapa: Filtro")
        
        plt.legend(loc='upper right')
        plt.show()
