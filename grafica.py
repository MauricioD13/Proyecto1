import matplotlib.pyplot as plt
import numpy as np
import sys


def guardar(archivo,time,voltage):
        labels=[]
        labels=archivo.readline().split(",")
        labels[1]=labels[1].replace("\n","")
        i=0
        for line in archivo:
        
                linea=line.split(",")
                time.append(float(linea[0]+"."+linea[1]))
                voltage.append(float(linea[2]+"."+linea[3]))
                i+=1
                if(i>=20000):
                        break  
                
        return labels
if(sys.argv[1]=="-ganancia"):
        archivo0=open("./datos/primera_etapa_entrada_diferencial_1mV.txt","r");
        archivo1=open("./datos/primera_etapa_filtro_1mV.txt","r");
        archivo2=open("./datos/segunda_etapa_filtro_1mV.txt","r");
        #~/Documents/Python/Proyecto/
        #parameter=sys.argv[1].split(".")

        #file_write=open(parameter[0]+"_fixed.txt","w")


        time0=[] 
        voltage0=[]
        time1=[] 
        voltage1=[]
        time2=[] 
        voltage2=[]

        labels0=guardar(archivo0,time0,voltage0)
        labels1=guardar(archivo1,time1,voltage1)
        labels2=guardar(archivo2,time2,voltage2)
        #file_write.write(linea[0]+"."+linea[1]+" "+linea[2]+"."+linea[3])
        archivo0.close()
        archivo1.close()
        archivo2.close()
        #file_write.close()
        time_array0=np.array(time0[1000:5000])
        voltage_array0=np.array(voltage0[1000:5000])
        time_array1=np.array(time1[1000:5000])
        voltage_array1=np.array(voltage1[1000:5000])

        time_array2=np.array(time2[1000:5000])
        voltage_array2=np.array(voltage2[1000:5000])

        fig, ax=plt.subplots()


        print("MUESTRAS:",len(time0))

        ax.plot(time_array0,voltage_array0,label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        plt.grid(True)
        ax.set_ylabel("Voltage")
        ax.set_xlabel(labels0[0])

        ax.plot(time_array0,voltage_array1,label="Segunda Etapa: Filtro")  # Plot some data on the axes.

        ax.plot(time_array0,voltage_array2,label="Tercera Etapa: Filtro")
        plt.legend(loc='upper left')

        #plt.grid(True)
        #ax[1].set_ylabel(labels1[1])
        #ax[1].set_xlabel(labels1[0])
        plt.show()
                    
elif(sys.argv[1]=="-manejo"):
        archivo0=open("./datos/primera_etapa_entrada_diferencial_30mV.txt","r");
        archivo1=open("./datos/primera_etapa_filtro_30mV.txt","r");
        archivo2=open("./datos/segunda_etapa_filtro_30mV.txt","r");
        #~/Documents/Python/Proyecto/
        #parameter=sys.argv[1].split(".")

        #file_write=open(parameter[0]+"_fixed.txt","w")


        time0=[] 
        voltage0=[]
        time1=[] 
        voltage1=[]
        time2=[] 
        voltage2=[]

        labels0=guardar(archivo0,time0,voltage0)
        labels1=guardar(archivo1,time1,voltage1)
        labels2=guardar(archivo2,time2,voltage2)
        archivo0.close()
        archivo1.close()
        archivo2.close()
        
        
        time_array0=np.array(time0[1000:5000])
        
        voltage_array0=np.array(voltage0[500:4500])
        
        voltage_array1=np.array(voltage1[1000:5000])

        
        voltage_array2=np.array(voltage2[1000:5000])

        fig, ax=plt.subplots(1,3)


        print("MUESTRAS:",len(time0))

        ax[0].plot(time_array0,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0].set_ylabel("Voltage")
        ax[0].set_xlabel(labels0[0])
        ax[0].set_title("Primera Etapa")
        ax[0].grid(True)
        
        
        
        ax[1].plot(time_array0,voltage_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        ax[1].set_title("Segunda Etapa")
        ax[1].grid(True)
        
        ax[2].set_title("Tercera Etapa")
        ax[2].plot(time_array0,voltage_array2,label="Tercera Etapa: Filtro")
        ax[2].grid(True)
        
        
       

        #plt.grid(True)
        #ax[1].set_ylabel(labels1[1])
        #ax[1].set_xlabel(labels1[0])
        plt.show()