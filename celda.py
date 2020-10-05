import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import statistics

def guardar(archivo,time,voltage0):
        labels=[]
        labels=archivo.readline().split("\t")
        #labels[1]=labels[1].replace("\n","")
        i=0
        for line in archivo:
                linea=line.split("\t")
                temp=linea[0].split(",")
                time.append(float(temp[0]+"."+temp[1]))
                temp=linea[1].split(",")
                temp[1]=temp[1].replace("\n","")
                voltage0.append(float(temp[0]+"."+temp[1]))
                i+=1
                
        return labels
option=input("Opcion=?: ")
if(option=="1"):
        archivo0=open("./datos/celda/CeldaCon0g.txt","r")
        archivo1=open("./datos/celda/CeldaCon10g.txt","r")
        archivo2=open("./datos/celda/CeldaCon20g.txt","r")
        archivo3=open("./datos/celda/CeldaCon100g.txt","r")
        archivo4=open("./datos/celda/CeldaCon200g.txt","r")
        archivo5=open("./datos/celda/CeldaCon500g.txt","r")

                
        time0=[] 
        voltage0=[]
        time1=[] 
        voltage1=[]
        time2=[] 
        voltage2=[]
        time3=[] 
        voltage3=[]
        time4=[] 
        voltage4=[]
        time5=[] 
        voltage5=[]
        guardar(archivo0,time0,voltage0)
        guardar(archivo1,time1,voltage1)
        guardar(archivo2,time2,voltage2)
        guardar(archivo3,time3,voltage3)
        guardar(archivo4,time4,voltage4)
        guardar(archivo5,time5,voltage5)
        archivo0.close()
                

                
        time_array0=np.array(time0[0:5000])
        voltage_array0=np.array(voltage0[0:5000])
        time_array1=np.array(time1[0:5000])
        voltage_array1=np.array(voltage1[0:5000])
        time_array2=np.array(time2[0:5000])
        voltage_array2=np.array(voltage2[0:5000])
        time_array3=np.array(time3[0:5000])
        voltage_array3=np.array(voltage3[0:5000])
        time_array4=np.array(time4[0:5000])
        voltage_array4=np.array(voltage4[0:5000])
        time_array5=np.array(time5[0:5000])
        voltage_array5=np.array(voltage5[0:5000])

        
        fig, ax=plt.subplots(2,3)


        print("MUESTRAS:",len(time0))

        ax[0,0].plot(time_array0,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0,0].set_ylabel("Voltaje [V]")
        ax[0,0].set_xlabel("Tiempo [s]")
        ax[0,0].set_title("0g")
        ax[0,0].grid(True)

        ax[0,1].plot(time_array1,voltage_array1,'g',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0,1].set_ylabel("Voltaje [V]")
        ax[0,1].set_xlabel("Tiempo [s]")
        ax[0,1].set_title("10g")
        ax[0,1].grid(True)

        ax[0,2].plot(time_array2,voltage_array2,'b',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0,2].set_ylabel("Voltaje [V]")
        ax[0,2].set_xlabel("Tiempo [s]")
        ax[0,2].set_title("20g")
        ax[0,2].grid(True)

        ax[1,0].plot(time_array3,voltage_array3,label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[1,0].set_ylabel("Voltaje [V]")
        ax[1,0].set_xlabel("Tiempo [s]")
        ax[1,0].set_title("100g")
        ax[1,0].grid(True)

        ax[1,1].plot(time_array4,voltage_array4,'y',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[1,1].set_ylabel("Voltaje [V]")
        ax[1,1].set_xlabel("Tiempo [s]")
        ax[1,1].set_title("200g")
        ax[1,1].grid(True)


        ax[1,2].plot(time_array5,voltage_array5,'o',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[1,2].set_ylabel("Voltaje [V]")
        ax[1,2].set_xlabel("Tiempo [s]")
        ax[1,2].set_title("500g")
        ax[1,2].grid(True)



        average0=np.mean(voltage_array0)
        average1=np.mean(voltage_array1)
        average2=np.mean(voltage_array2)
        average3=np.mean(voltage_array3)
        average4=np.mean(voltage_array4)
        average5=np.mean(voltage_array5)
        print(average0,average1,average2,average3,average4,average5)
        mplcursors.cursor()
        plt.show()
if(option=="2"):
        archivo0=open("./datos/ImpedanciaEntrada.txt","r")

        time0=[]
        voltage0=[]

        guardar(archivo0,time0,voltage0)
        time_array0=np.array(time0[0:10000])
        voltage_array0=np.array(voltage0[0:10000])

        fig, ax=plt.subplots()

        ax.plot(time_array0,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax.set_ylabel("Voltaje [V]")
        ax.set_xlabel("Tiempo")
        ax.set_title("Impedancia de entrada")
        ax.grid(True)

        plt.show()