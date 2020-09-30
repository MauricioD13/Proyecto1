import matplotlib.pyplot as plt
import numpy as np
import sys



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
if(sys.argv[1]=="-ganancia"):
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
            #file_write.write(linea[0]+"."+linea[1]+" "+linea[2]+"."+linea[3])
    archivo0.close()
    print(time0[100:150])
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