import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import statistics
import mplcursors

def guardar(archivo,time,voltage0,voltage1,voltage2):
        labels=[]
        labels=archivo.readline().split("\t")
        #labels[1]=labels[1].replace("\n","")
        i=0
        for line in archivo:
                linea=line.split("\t")
                temp=linea[0].split(",")
                time.append(float(temp[0]+"."+temp[1]))
                temp=linea[1].split(",")
                voltage0.append(float(temp[0]+"."+temp[1]))
                temp=linea[3].split(",")
                voltage1.append(float(temp[0]+"."+temp[1]))
                temp=linea[5].split(",")
                voltage2.append(float(temp[0]+"."+temp[1]))
                i+=1
                if(i>=20000):
                        break  
                
        return labels
option=input("Opcion?: ")
if(option=="ganancia"):
    archivo0=open("./datos/Ganancia_1mV_80Hz.txt","r");
            #~/Documents/Python/Proyecto/
            #parameter=sys.argv[1].split(".")
            #file_write=open(parameter[0]+"_fixed.txt","w")


    time0=[] 
    voltage0=[]
    time1=[] 
    voltage1=[]
    time2=[] 
    voltage2=[]

    labels0=guardar(archivo0,time0,voltage0,voltage1,voltage2)
    archivo0.close()
   
    time_array0=np.array(time0[1000:5000])
    voltage_array0=np.array(voltage0[1000:5000])
    time_array1=np.array(time1[1000:5000])
    voltage_array1=np.array(voltage1[1000:5000])

    time_array2=np.array(time2[1000:5000])
    voltage_array2=np.array(voltage2[1000:5000])

    fig, ax=plt.subplots(3,1)
    fig.subplots_adjust(hspace=0.5)    

    print("MUESTRAS:",len(time0))    
    ax[0].plot(time_array0,voltage_array0,label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
    ax[0].grid(True)
    ax[0].set_ylabel("Voltage")
    ax[0].set_xlabel("Tiempo")
    ax[0].set(ylim=(1,3))
    ax[0].set_title("Primera Etapa")    

    ax[1].plot(time_array0,voltage_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
    ax[1].grid(True)
    ax[1].set_ylabel("Voltage")
    ax[1].set_xlabel("Tiempo")
    ax[1].set(ylim=(1,3))
    ax[1].set_title("Segunda Etapa") 

    ax[2].plot(time_array0,voltage_array2,'r',label="Tercera Etapa: Filtro")
    ax[2].grid(True)
    ax[2].set_ylabel("Voltage")
    ax[2].set_xlabel("Tiempo")
    ax[2].set(ylim=(1,3))
    ax[2].set_title("Tercera Etapa") 
    

        
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    
    plt.show()
elif(option=="manejo"):
        archivo0=open("./datos/Manejo_80Hz_30mV.txt","r");
        
        #~/Documents/Python/Proyecto/
        #parameter=sys.argv[1].split(".")

        #file_write=open(parameter[0]+"_fixed.txt","w")


        time0=[] 
        voltage0=[]
        time1=[] 
        voltage1=[]
        time2=[] 
        voltage2=[]

        labels0=guardar(archivo0,time0,voltage0,voltage1,voltage2)
        archivo0.close()
        
        
        
        time_array0=np.array(time0[0:500])
        
        voltage_array0=np.array(voltage0[0:500])
        
        voltage_array1=np.array(voltage1[0:500])

        
        voltage_array2=np.array(voltage2[0:500])
        fig, ax=plt.subplots(1,3)


        print("MUESTRAS:",len(time0))

        ax[0].plot(time_array0,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0].set_ylabel("Voltage")
        ax[0].set_xlabel("Tiempo")
        ax[0].set_title("Primera Etapa")
        ax[0].grid(True)
        ax[0].set(ylim=(0,5.5))
        
        
        ax[1].plot(time_array0,voltage_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        ax[1].set_title("Segunda Etapa")
        ax[1].grid(True)
        ax[1].set(ylim=(0,5.5))
        ax[1].set_ylabel("Voltage")
        ax[1].set_xlabel("Tiempo")


        ax[2].set_title("Tercera Etapa")
        ax[2].plot(time_array0,voltage_array2,label="Tercera Etapa: Filtro")
        ax[2].grid(True)
        ax[2].set(ylim=(0,5.5))
        ax[2].set_ylabel("Voltage")
        ax[2].set_xlabel("Tiempo")
        
        
        

        #plt.grid(True)
        #ax[1].set_ylabel(labels1[1])
        #ax[1].set_xlabel(labels1[0])
        mplcursors.cursor()
        plt.show()
elif(option=="comun"):
    archivo0=open("./datos/Ganancia_comun_1mV_80Hz.txt","r");

    time_common=[] 
    voltage_common=[]
    labels=[]
    labels=archivo0.readline().split("\t")
    for line in archivo0:
                linea=line.split("\t")
                temp=linea[0].split(",")
                time_common.append(float(temp[0]+"."+temp[1]))
                temp=linea[1].split(",")
                voltage_common.append(float(temp[0]+"."+temp[1]))



    archivo0.close()
    time_array0=np.array(time_common[0:5000])
    voltage_array0=np.array(voltage_common[0:5000])
    average=0
    for i in time_common:
            average=i+average
    average=average/len(time_common)
    fig, ax=plt.subplots()
    common_gain=(average/0.001)-200
    print(f"MUESTRAS:{len(time_common)}, Promedio: {average}: Ganancia comun: {common_gain} CMRR:{20*math.log10(1000/common_gain)}")

    ax.plot(time_array0,voltage_array0,label="Entrada modo comun")  # Plot some data on the axes.
    plt.grid(True)
    ax.set_ylabel("Voltage")
    ax.set_xlabel("Tiempo")
    plt.legend(loc='upper left')

    plt.show()

elif(option=="ruido"):
    archivo0=open("./datos/Distorsión_1m_80Hz.txt","r");

    time_common=[] 
    voltage_common=[]
    labels=[]
    labels=archivo0.readline().split("\t")
    for line in archivo0:
                linea=line.split("\t")
                temp=linea[0].split(",")
                time_common.append(float(temp[0]+"."+temp[1]))
                temp=linea[1].split(",")
                voltage_common.append(float(temp[0]+"."+temp[1]))



    archivo0.close()
    time_array0=np.array(time_common[0:1000])
    voltage_array0=np.array(voltage_common[0:1000])
    average=0
    for i in time_common:
            average=i+average
    average=average/len(time_common)
    fig, ax=plt.subplots()
    common_gain=(average/0.001)-200
    print(f"MUESTRAS:{len(time_common)}, Promedio: {average}: Ganancia comun: {common_gain} CMRR:{20*math.log10(1000/common_gain)}")

    ax.plot(time_array0,voltage_array0)  # Plot some data on the axes.
    plt.grid(True)
    ax.set_ylabel("Potencia [dB]")
    ax.set_title("Power Spectrum")
    ax.set_xlabel("Frecuencia [Hz]")
    mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
    
    plt.show()

