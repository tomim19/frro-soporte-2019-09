## 4. Ejercicio al Formulario del Ejercicio 3 ,  agrege  los siguientes botones 1- un  botón  Alta 
## que inicia otra venta donde puedo ingresar una ciudad y su código postal .
## 2 – un botón Baja que borra del listad de ciudades la ciudad que esta selecionada en Treeview .
## 3 – un botón Modificar . Todos los cambios se deben ver reflejados en la lista que se muestra . 

from tkinter import *
from tkinter import ttk


class Aplicacion():

        def __init__(self):
                self.raiz = Tk()
                self.raiz.title("Ciudades y codigos postales")
                self.tree = ttk.Treeview(self.raiz)
#Variable
                self.ciu=StringVar()
                self.cp=IntVar()
                self.i = 0
#Columnas
                self.tree["columns"]=("one","two")
                self.tree.column("#0", width=100)
                self.tree.column("one", width=100 )
                self.tree.column("two", width=100)
                self.tree.heading("#0", text="Id")
                self.tree.heading("one", text="Ciudad")
                self.tree.heading("two", text="Codigo Postal")
#Insert
                self.boton0 = ttk.Button(self.raiz, text="Agregar", command=self.grilla)
                self.boton1 = ttk.Button(self.raiz, text="Eliminar", command=self.Baja) 
                self.boton2 = ttk.Button(self.raiz, text="Modificar", command=self.grilla2) 
                self.boton0.grid(row=1, column=5)
                self.boton1.grid(row=2, column=5)
                self.boton2.grid(row=3, column=5)               
#Loop
                self.tree.grid()
                self.raiz.mainloop()
#Alta
        def Agrega(self):
                self.tree.insert('', 'end', text=str(self.i), values=(self.ciu.get(), self.cp.get()),iid=self.i)
                self.i = self.i + 1

        def grilla(self):
                self.ventana = Toplevel()
                self.ventana.title("Nueva ciudad")
                self.label0 = ttk.Label(self.ventana, text="Ciudad: ")
                self.label1 = ttk.Label(self.ventana, text="Codigo postal:")
                self.entry0 = ttk.Entry(self.ventana, textvariable=self.ciu, width=30)
                self.entry1 = ttk.Entry(self.ventana, textvariable=self.cp, width=30)
                self.boton0 = ttk.Button(self.ventana, text="Agregar", command=self.Agrega)
                self.label0.grid(row=0, column=0)
                self.label1.grid(row=1, column=0)
                self.entry0.grid(row=0, column=1)
                self.entry1.grid(row=1, column=1)
                self.boton0.grid(row=2, column=2)
#Baja       
        def Baja(self):
                selected_item = self.tree.selection()[0]
                self.tree.delete(selected_item)
#Modificacion
        def Modificar(self):
                x = self.tree.selection()[0]
                for item in x:
                        self.tree.item(item, values=(self.ciu.get(), self.cp.get()))

        def grilla2(self):
                self.ventana = Toplevel()
                self.ventana.title("Modificar ciudad")
                self.label0 = ttk.Label(self.ventana, text="Ciudad: ")
                self.label1 = ttk.Label(self.ventana, text="Codigo postal:")
                self.entry0 = ttk.Entry(self.ventana, textvariable=self.ciu, width=30)
                self.entry1 = ttk.Entry(self.ventana, textvariable=self.cp, width=30)
                self.boton0 = ttk.Button(self.ventana, text="Modificar", command=self.Modificar)
                self.label0.grid(row=0, column=0)
                self.label1.grid(row=1, column=0)
                self.entry0.grid(row=0, column=1)
                self.entry1.grid(row=1, column=1)
                self.boton0.grid(row=2, column=2)        



def main():
    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()