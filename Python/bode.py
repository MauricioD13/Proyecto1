import matplotlib.pyplot as plt
import numpy as np
import mplcursors


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
                if(i>=20000):
                        break  
                
        return labels
option=input("Opcion?")
if(option=="1"):
        archivo0=open("./datos/BodeTotal_80Hz_1mV_10_1.5k.txt","r")
        archivo1=open("./datos/BodeEtapa2_80Hz_1mV_10_1.5k.txt","r")
        archivo2=open("./datos/BodeEtapa1_10Hz_15mV_10_20k.txt","r")

                
        frequency0=[] 
        voltage0=[]
        frequency1=[] 
        voltage1=[]
        frequency2=[] 
        voltage2=[]
        labels0=guardar(archivo2,frequency0,voltage0)
        labels0=guardar(archivo1,frequency1,voltage1)
        labels0=guardar(archivo0,frequency2,voltage2)
        archivo0.close()
                

                
        frequency_array0=np.array(frequency0[0:100])
        frequency_array1=np.array(frequency1[1:100])
        frequency_array2=np.array(frequency2[0:100])
                
        voltage_array0=np.array(voltage0[0:100])
                
        voltage_array1=np.array(voltage1[1:100])

                
        voltage_array2=np.array(voltage2[0:100])
        fig, ax=plt.subplots(1,3)


        print("MUESTRAS:",len(frequency0))

        ax[0].plot(frequency_array0,voltage_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0].set_ylabel("Magnitud [dB]")
        ax[0].set_xlabel("Frecuencia [Hz]")
        ax[0].set_title("Primera Etapa")
        ax[0].grid(True)
        ax[0].set(xlim=(0,300))
                
                
        ax[1].plot(frequency_array1,voltage_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        ax[1].set_title("Segunda Etapa")
        ax[1].grid(True)
        ax[1].set_ylabel("Magnitud [dB]")
        ax[1].set_xlabel("Frecuencia [Hz]")
        ax[1].set(xlim=(0,300))



        ax[2].set_title("Tercera Etapa")
        ax[2].plot(frequency_array2,voltage_array2,label="Tercera Etapa: Filtro")
        ax[2].grid(True)

        ax[2].set_ylabel("Magnitud [dB]")
        ax[2].set_xlabel("Frecuencia [Hz]")
        ax[2].set(xlim=(0,300))
                
                
                

                #plt.grid(True)
                #ax[1].set_ylabel(labels1[1])
                #ax[1].set_xlabel(labels1[0])
        mplcursors.cursor()
        plt.show()
if(option=="2"):
        archivo0=open("./datos/BodeTotal_80Hz_1mV_10_1.5k.txt","r");
        archivo1=open("./datos/BodeModoComún10mV_1.txt","r");
        
                
        frequency0=[] 
        gain0=[]
        frequency1=[] 
        gain1=[]
        labels0=guardar(archivo0,frequency0,gain0)
        labels0=guardar(archivo1,frequency1,gain1)
        archivo0.close()
                

                
        frequency_array0=np.array(frequency0[0:150])
        frequency_array1=np.array(frequency1[0:150])
        
                
        gain_array0=np.array(gain0[0:150])
                
        gain_array1=np.array(gain1[0:150])

                
        
        fig, ax=plt.subplots(1,3)


        print("MUESTRAS:",len(frequency0))

        ax[0].plot(frequency_array0,gain_array0,'r',label="Primera Etapa: Entrada diferencial")  # Plot some data on the axes.
        ax[0].set_ylabel("Magnitud")
        ax[0].set_xlabel("Frecuencia")
        ax[0].set_title("Bode modo diferencial")
        ax[0].grid(True)
                
                
        ax[1].plot(frequency_array1,gain_array1,'g',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        ax[1].set_title("Bode modo comun")
        ax[1].grid(True)
        ax[1].set_ylabel("Magnitud")
        ax[1].set_xlabel("frecuencia")
        CMRR=[]
        for i in range(0,150):
                CMRR.append(gain0[i]-gain1[i])
        CMRR_array=np.array(CMRR)
        ax[2].plot(frequency_array1,CMRR_array,'b',label="Segunda Etapa: Filtro")  # Plot some data on the axes.
        ax[2].set_title("CMRR")
        ax[2].grid(True)
        ax[2].set_ylabel("Magnitud")
        ax[2].set_xlabel("frecuencia")
          

        mplcursors.cursor()
        plt.show()
if(option=="3"):
        archivo0=open("./datos/GananciaPSRR.txt","r")
        

                
        frequency0=[] 
        voltage0=[]
        frequency1=[] 
        voltage1=[]
        frequency2=[] 
        voltage2=[]
        labels0=guardar(archivo0,frequency0,voltage0)
        archivo0.close()
                

                
        frequency_array0=np.array(frequency0[0:100])
                
        voltage_array0=np.array(voltage0[0:100])
                
        fig, ax=plt.subplots()


        print("MUESTRAS:",len(frequency0))

        ax.plot(frequency_array0,voltage_array0,'r',label="PSRR")  # Plot some data on the axes.
        ax.set_ylabel("Magnitud [dB]")
        ax.set_xlabel("Frecuencia [Hz]")
        ax.set_title("PSRR")
        ax.grid(True)

        plt.show()
        
                
