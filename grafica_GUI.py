from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os
import grafica_procesamiento

window0=Tk()
window0.title("GRAFICADOR")
window0.geometry("700x600")


def openfile():
    number=0
    cwd=os.getcwd()
    file_name=filedialog.askopenfilename(initialdir=cwd,title="Seleccione archivo",filetypes= (("archivo de texto","*.txt"),("CSV","*.csv")))
    while(True):
        try:
            tree.insert('','end',iid=number,text=str(number),value=(file_name,"0"))
            break
        except TclError:
            number=number+1
           
def process():
    i=0
    files_name=[]
    while(True):
        files_name.append(tree.item(i)['values'][0])
        if tree.next(i):
            i+=1
        else:
            break
    grafica_procesamiento.graphics(files_name,separator_entry.get(),number_separator_entry.get(),selection_entry.get(),name_entry.get(),x_entry.get(),y_entry.get())
    

#Objects
tree=ttk.Treeview(window0,columns=("File"))

separator_label=Label(window0,text="Separador de datos")
separator_entry=Entry(window0,width=10)

number_separator_label=Label(window0,text="Separador de numero")
number_separator_entry=Entry(window0,width=10)

selection_label=Label(window0,text="Organizacion")
selection_entry=Entry(window0)

name_label=Label(window0,text="Nombre de la grafica")
name_entry=Entry(window0)

x_label=Label(window0,text="Titulo eje X")
x_entry=Entry(window0)

y_label=Label(window0,text="Titulo eje Y")
y_entry=Entry(window0)

Button(text="Abrir archivo",command=openfile).place(x=10,y=420)
Button(text="Procesar",command=process).place(x=150,y=420)


tree.heading('#0',text="ID")
tree.heading('#1',text="File")
tree.column('#0', stretch=NO)
tree.column('#1', stretch=NO,width=400)


selection_label.place(x=300,y=400)
selection_entry.place(x=300,y=420)

name_label.place(x=450,y=400)
name_entry.place(x=450,y=420)
separator_label.place(x=10,y=300)
separator_entry.place(x=10,y=320)

number_separator_label.place(x=150,y=300)
number_separator_entry.place(x=150,y=320)

x_label.place(x=300,y=300)
x_entry.place(x=300,y=320)

y_label.place(x=400,y=300)
y_entry.place(x=400,y=320)

tree.grid(row=1, columnspan=3, sticky='nsew')




window0.mainloop()









