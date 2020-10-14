import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import statistics
import mplcursors



def graphics(nombres_archivo,separator,number_separator,organization,name,x_label,y_label):

        files=[]
        legend_names=[]
        temp=[]
        for i in range(len(nombres_archivo)):
                temp=nombres_archivo[i].split("/")
                legend_names.append(temp[len(temp)-1])
        
        print(legend_names)
        for i in range(len(nombres_archivo)):
            archivo=open(nombres_archivo[i],"r")
            files.append(archivo)
        if(len(files)<=3):
                
                i=0
                time_array=[]
                voltage_array=[]
                if(number_separator==","):
                        lenghts=[]
                        for i in range(len(files)):
                                
                                if(separator==","):
                                        labels=[]
                                        labels=files[i].readline().split(separator)
                                        temp_time=[]
                                        temp_voltage=[]
                                        for line in files[i]:
                                                linea=line.split(separator)
                                                temp_time.append(float(linea[0]+"."+linea[1]))
                                                temp_voltage.append(float(linea[2]+"."+linea[3]))
                                                i+=1
                                                if(i>=20000):
                                                        break 
                                        lenghts.append(len(temp_time))
                                        time_array.append(np.array(temp_time))
                                        voltage_array.append(np.array(temp_voltage))
                                else:
                                        labels=[]
                                        labels=files[i].readline().split(separator)
                                        temp_time=[]
                                        print(separator)
                                        if(separator=="tab"):
                                                separator="\t"
                                        temp_voltage=[]
                                        for line in files[i]:
                                                linea=line.split(str(separator))
                                                temp=linea[0].split(number_separator)
                                                temp_time.append(float(temp[0]+"."+temp[1]))
                                                temp=linea[1].split(number_separator)
                                                temp_voltage.append(float(temp[0]+"."+temp[1]))
                                                i+=1
                                                if(i>=20000):
                                                        break
                                        lenghts.append(len(temp_time)) 
                                        time_array.append(np.array(temp_time))
                                        voltage_array.append(np.array(temp_voltage))

                        graphic_quantity=organization.split(";")
                        graphics_inside=graphic_quantity[0].split(",")
                        print(lenghts)
                        if(len(graphic_quantity)>1):
                                fig, ax=plt.subplots(1,len(graphic_quantity))
                                for i in range(len(graphic_quantity)):
                                        for j in range(len(graphics_inside)):  
                                                ax[i].plot(time_array[j][0:min(lenghts)],voltage_array[j][min(lenghts)],label=name)  # Plot some data on the axes.
                                                ax[i].grid(True)
                                                ax[i].set_ylabel(y_label)
                                                ax[i].set_xlabel(x_label)
                                                ax[i].set_title(name)   
                        else:
                                fig, ax=plt.subplots()
                                for j in range(len(graphics_inside)):  
                                                ax.plot(time_array[j][0:min(lenghts)],voltage_array[j][0:min(lenghts)],label=legend_names[j])  # Plot some data on the axes.
                                                ax.grid(True)
                                                ax.set_ylabel(y_label)
                                                ax.set_xlabel(x_label)
                                                ax.set_title(name) 
                                                ax.legend(loc="upper right")
                        fig.subplots_adjust(hspace=0.5)
                        
                        
                         
                        mplcursors.cursor(multiple=True).connect(
                        "add", lambda sel: sel.annotation.draggable(False))
                        
                        plt.show()
                if(number_separator=="."):
                        
                        for i in range(len(files)):
                                labels=[]
                                labels=files[i].readline().split(separator)
                                temp_time=[]
                                temp_voltage=[]
                                for line in archivo:
                                        linea=line.split(separator)
                                        temp=linea.split(number_separator)
                                        temp_time.append(float(temp[0]+"."+temp[1]))
                                        temp_voltage.append(float(temp[0]+"."+temp[1]))
                                        i+=1
                                        if(i>=20000):
                                                break
                                time_array.append(np.array(temp_time))
                                voltage_array.append(np.array(temp_voltage))
                        graphic_quantity=organization.split(";")
                        columns=graphic_quantity[0].split(",")
                        
                        if(len(graphic_quantity)>1):
                                fig, ax=plt.subplots(1,len(graphic_quantity))
                                for i in range(len(graphic_quantity)):
                                        for j in range(len(columns)):  
                                                ax[i].plot(time_array[j],voltage_array[j],label=name)  # Plot some data on the axes.
                                                ax[i].grid(True)
                                                ax[i].set_ylabel(y_label)
                                                ax[i].set_xlabel(x_label)
                                                ax[i].set_title(name)   
                        else:
                                fig, ax=plt.subplots()
                                for j in range(len(columns)):  
                                                ax.plot(time_array[j],voltage_array[j],label=name)  # Plot some data on the axes.
                                                ax.grid(True)
                                                ax.set_ylabel(y_label)
                                                ax.set_xlabel(x_label)
                                                ax.set_title(name)
                        plt.show()
        if(len(files)>3):
                        #labels[1]=labels[1].replace("\n","")
                i=0
                time_array=[]
                voltage_array=[]
                if(number_separator==","):
                        for i in range(len(files)):
                                labels=[]
                                labels=files[i].readline().split(separator)
                                temp_time=[]
                                temp_voltage=[]
                                for line in files[i]:
                                        linea=line.split(separator)
                                        temp_time.append(float(linea[0]+"."+linea[1]))
                                        temp_voltage.append(float(linea[2]+"."+linea[3]))
                                        i+=1
                                        if(i>=20000):
                                                break 
                                time_array.append(np.array(temp_time))
                                voltage_array.append(np.array(temp_voltage))
                                
                        graphic_rows=organization.split(";")
                        graphic_columns=graphic_rows[0].split(",")
                        
                        
                        fig, ax=plt.subplots(len(graphic_rows),len(graphic_columns))
                        
                        for j in range(len(graphic_rows)):
                                for i in range(len(graphic_columns)):
                                        ax[j][i].plot(time_array[i],voltage_array[i],label=name)  # Plot some data on the axes.
                                        ax[j][i].grid(True)
                                        ax[j][i].set_ylabel(y_label)
                                        ax[j][i].set_xlabel(x_label)
                                        ax[j][i].set_title(name)    
                        mplcursors.cursor(multiple=True).connect("add", lambda sel: sel.annotation.draggable(False))
    
                        plt.show()
                if(number_separator=="."):
                        
                        for i in range(len(files)):
                                labels=[]
                                labels=files[i].readline().split(separator)
                                temp_time=[]
                                temp_voltage=[]
                                for line in archivo:
                                        linea=line.split(separator)
                                        temp=linea.split(number_separator)
                                        temp_time.append(float(temp[0]+"."+temp[1]))
                                        temp_voltage.append(float(temp[0]+"."+temp[1]))
                                        i+=1
                                        if(i>=20000):
                                                break
                                time_array.append(np.array(temp_time))
                                voltage_array.append(np.array(temp_voltage))
                        rows=[]
                        rows=organization.split(";")
                        print(rows)
                        fig, ax=plt.subplots(len(files)/2,len(files)/2)
                        
                        for j in range(len(files)/2):
                                for i in range(len(files)/2):
                                        ax[j][i].plot(time_array[i],voltage_array[i],label=name)  # Plot some data on the axes.
                                        ax[j][i].grid(True)
                                        ax[j][i].set_ylabel(y_label)
                                        ax[j][i].set_xlabel(x_label)
                                        ax[j][i].set_title(name)    
                        mplcursors.cursor(multiple=True).connect("add", lambda sel: sel.annotation.draggable(False))
    
                        plt.show()
        
                
                

