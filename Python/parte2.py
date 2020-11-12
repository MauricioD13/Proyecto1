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
if(option=="1"):
        archivo0=open("./datos/Parte 2 frec sin c.csv","r")
        archivo1=open("./datos/Parte 2 frec con c tantalio 10u.csv","r")
        archivo2=open("./datos/Parte 2 frec con c poliester 1u.csv","r")
        archivo3=open("./datos/parte 2 Frec con c electrolitico 10u.csv","r")
        frequency0=[]
        frequency1=[]
        frequency2=[]
        frequency3=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]
        voltage3=[]

        guardar(archivo0,frequency0,voltage0)
        guardar(archivo1,frequency1,voltage1)
        guardar(archivo2,frequency2,voltage2)
        guardar(archivo3,frequency3,voltage3)


        frequency_array0=np.array(frequency0)
        frequency_array1=np.array(frequency1)
        frequency_array2=np.array(frequency2)
        frequency_array3=np.array(frequency3)


        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        voltage_array2=np.array(voltage2)
        voltage_array3=np.array(voltage3)


        fig, ax=plt.subplots(2,2)
        ax[0,0].plot(frequency_array0,voltage_array0,'g',label="Respuesta en frecuencia sin condensador")
        ax[0,0].set_xlabel("Frecuencia")
        ax[0,0].set_ylabel("Magnitud [dB]")
        ax[0,0].grid(True)
        ax[0,0].legend(loc='upper right')

        ax[1,0].plot(frequency_array1,voltage_array1,'r',label="Respuesta en frecuencia condensador de tantalio") 
        ax[1,0].set_xlabel("Frecuencia")
        ax[1,0].set_ylabel("Magnitud [dB]")
        ax[1,0].grid(True)
        ax[1,0].legend(loc='upper right')

        ax[1,1].plot(frequency_array2,voltage_array2,'b',label="Respuesta en frecuencia condensador de poliester")  
        ax[1,1].set_xlabel("Frecuencia")
        ax[1,1].set_ylabel("Magnitud [dB]")
        ax[1,1].grid(True)
        ax[1,1].legend(loc='upper right')

        ax[0,1].plot(frequency_array3,voltage_array3,label="Respuesta en frecuencia condensador de electrolitico")  
        ax[0,1].set_xlabel("Frecuencia")
        ax[0,1].set_ylabel("Magnitud [dB]")
        mplcursors.cursor()
        ax[0,1].grid(True)
        ax[0,1].legend(loc='upper right')


        mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
        plt.grid(True)
        plt.show()
elif(option=="2"):
        archivo0=open("./datos/vb0 poliester.csv","r")
        archivo1=open("./datos/vb0 tantalio.csv","r")
        archivo2=open("./datos/vbc.csv","r")
        archivo3=open("./datos/vbc1.csv","r")
        frequency0=[]
        frequency1=[]
        frequency2=[]
        frequency3=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]
        voltage3=[]

        guardar(archivo0,frequency0,voltage0)
        guardar(archivo1,frequency1,voltage1)
        guardar(archivo2,frequency2,voltage2)
        guardar(archivo3,frequency3,voltage3)


        frequency_array0=np.array(frequency0)
        frequency_array1=np.array(frequency1)
        frequency_array2=np.array(frequency2)
        frequency_array3=np.array(frequency3)


        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        voltage_array2=np.array(voltage2)
        voltage_array3=np.array(voltage3)

        xlabel="Tiempo"
        ylabel="Voltaje"
        fig, ax=plt.subplots(2,2)
        ax[0,0].plot(frequency_array0,voltage_array0,'g',label="Voltaje B-GND Poliester")
        ax[0,0].set_xlabel(xlabel)
        ax[0,0].set_ylabel(ylabel)
        ax[0,0].grid(True)
        ax[0,0].legend(loc='upper right')

        ax[1,0].plot(frequency_array1,voltage_array1,'r',label="Voltaje B-GND Tantalio") 
        ax[1,0].set_xlabel(xlabel)
        ax[1,0].set_ylabel(ylabel)
        ax[1,0].grid(True)
        ax[1,0].legend(loc='upper right')

        ax[1,1].plot(frequency_array2,voltage_array2,'b',label="Voltaje B-C")  
        ax[1,1].set_xlabel(xlabel)
        ax[1,1].set_ylabel(ylabel)
        ax[1,1].grid(True)
        ax[1,1].legend(loc='upper right')

        ax[0,1].plot(frequency_array3,voltage_array3,label="Voltaje B-C")  
        ax[0,1].set_xlabel(xlabel)
        ax[0,1].set_ylabel(ylabel)
        mplcursors.cursor()
        ax[0,1].grid(True)
        ax[0,1].legend(loc='upper right')


        mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
        plt.grid(True)
        plt.show()

elif(option=="3"):
        archivo0=open("./datos/vb0 poliester.csv","r")
        archivo1=open("./datos/scope_8.csv","r")

        frequency0=[]
        frequency1=[]
        voltage0=[]
        voltage1=[]
        guardar(archivo0,frequency0,voltage0)
        guardar(archivo1,frequency1,voltage1)

        frequency_array0=np.array(frequency0)
        frequency_array1=np.array(frequency1)
        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)

        fig, ax=plt.subplots(1,2)
        xlabel=("Tiempo")
        ylabel=("Voltaje")

        ax[0].plot(frequency_array0,voltage_array0,'g',label="Voltaje B-GND Poliester")
        ax[0].set_xlabel(xlabel)
        ax[0].set_ylabel(ylabel)
        ax[0].set_title("Voltaje B-C sin condensador")
        ax[0].grid(True)
        
        

        ax[1].plot(frequency_array1,voltage_array1,'r',label="Voltaje B-GND Tantalio") 
        ax[1].set_xlabel(xlabel)
        ax[1].set_ylabel(ylabel)
        ax[1].set_title("Voltaje B-GND sin condensador")
        ax[1].grid(True)
        ax[1].set(xlim=(-0.0001,0.0001))
        

        plt.show()
elif(option=="4"):
        archivo0=open("./datos/modelo propuesto (15u).csv","r")
        archivo1=open("./datos/modelo propuesto (15u) con c 10uF.csv","r")
        archivo2=open("./datos/modelo propuesto (15u) con c 1uF.csv","r")


        frequency0=[]
        frequency1=[]
        frequency2=[]
        voltage0=[]
        voltage1=[]
        voltage2=[]
        guardar(archivo0,frequency0,voltage0)
        guardar(archivo1,frequency1,voltage1)
        guardar(archivo2,frequency2,voltage2)

        frequency_array0=np.array(frequency0)
        frequency_array1=np.array(frequency1)
        frequency_array2=np.array(frequency2)
        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        voltage_array2=np.array(voltage2)

        fig, ax=plt.subplots(1,3)
        xlabel=("Tiempo")
        ylabel=("Voltaje")
        ax[0].plot(frequency_array0,voltage_array0,'g',label="Modelo propuesto")
        ax[0].set_xlabel(xlabel)
        ax[0].set_ylabel(ylabel)
        ax[0].set_title("Modelo propuesto")
        ax[0].grid(True)
        ax[0].set(xlim=(0.000045,0.00005))
        
        

        ax[1].plot(frequency_array1,voltage_array1,'r',label="Modelo propuesto con condensador 10uF") 
        ax[1].set_xlabel(xlabel)
        ax[1].set_ylabel(ylabel)
        ax[1].set_title("Modelo propuesto con condensador 10uF")
        ax[1].grid(True)
        ax[1].set(xlim=(0.000045,0.00005))
        
        ax[2].plot(frequency_array2,voltage_array2,label="Modelo propuesto con condensador 1uF") 
        ax[2].set_xlabel(xlabel)
        ax[2].set_ylabel(ylabel)
        ax[2].set_title("Modelo propuesto con condensador 1uF")
        ax[2].grid(True)
        ax[2].set(xlim=(0.000045,0.00005))
        mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
     
        
        plt.show()
elif(option=="5"):
        archivo0=open("./datos/a-0.csv","r")
        archivo1=open("./datos/b-c.csv","r")


        frequency0=[]
        frequency1=[]
        voltage0=[]
        voltage1=[]
        guardar(archivo0,frequency0,voltage0)
        guardar(archivo1,frequency1,voltage1)

        frequency_array0=np.array(frequency0)
        frequency_array1=np.array(frequency1)
        
        voltage_array0=np.array(voltage0)
        voltage_array1=np.array(voltage1)
        

        fig, ax=plt.subplots(1,2)
        xlabel=("Tiempo")
        ylabel=("Voltaje")
        ax[0].plot(frequency_array0,voltage_array0,'g',label="Voltaje A-GND")
        ax[0].set_xlabel(xlabel)
        ax[0].set_ylabel(ylabel)
        ax[0].set_title("Voltaje A-GND")
        ax[0].grid(True)
        #ax[0].set(xlim=(0.000045,0.00005))
        
        

        ax[1].plot(frequency_array1,voltage_array1,'r',label="Voltaje B-C") 
        ax[1].set_xlabel(xlabel)
        ax[1].set_ylabel(ylabel)
        ax[1].set_title("Voltaje B-C")
        ax[1].grid(True)
        #ax[1].set(xlim=(0.000045,0.00005))
        
        
        mplcursors.cursor(multiple=True).connect(
        "add", lambda sel: sel.annotation.draggable(False))
     
        
        plt.show()