from tkinter import *
from tkinter import ttk
import sys
sys.path.append("C:\SOPORTEV\GIT\practico_06")
sys.path.append("C:\SOPORTEV\GIT\practico_05")
from capa_negocio import NegocioSocio
from ejercicio_01 import Socio, Base, engine



class Aplicacion():

        def __init__(self):
                Base.metadata.bind = engine
                self.raiz = Tk()
                self.raiz.title("Gestion de Socios")
                self.tree = ttk.Treeview(self.raiz)
#Variable

                self.CN = NegocioSocio()
                self.Dni=IntVar()
                self.Nombre=StringVar()
                self.Apellido=StringVar()
#Columnas
                self.tree["columns"]=("one","two","three")
                self.tree.column("#0", width=100)
                self.tree.column("one", width=100 )
                self.tree.column("two", width=100)
                self.tree.column("three", width=100)
                self.tree.heading("#0", text="Id")
                self.tree.heading("one", text="Dni")
                self.tree.heading("two", text="Nombre")
                self.tree.heading("three", text="Apellido")
#Insert

                self.boton0 = ttk.Button(self.raiz, text="Agregar", command=self.grilla)
                self.boton1 = ttk.Button(self.raiz, text="Eliminar", command=self.Baja) 
                self.boton2 = ttk.Button(self.raiz, text="Modificar", command=self.grilla2) 
                self.boton0.grid(row=1, column=5)
                self.boton1.grid(row=2, column=5)
                self.boton2.grid(row=3, column=5)
                lista=self.CN.todoss() 
                for i in lista:
                     self.tree.insert('', 'end', text=str(i.id), values=(i.dni, i.nombre, i.apellido),iid=i.id)   
                self.CN.cerrar()              
#Loop

                self.tree.grid()
                self.raiz.mainloop()
#Alta
        def Agrega(self):
                dni = self.Dni.get()
                nombre = self.Nombre.get()
                apellido = self.Apellido.get()
                print(dni,nombre,apellido)
                socio = Socio(dni=dni, nombre=nombre, apellido=apellido)
                print(socio)
                bandera = self.CN.alta(socio)
                print(bandera)
                if (bandera==True):   
                    usu = self.CN.buscar_dni(dni) 
                    self.tree.insert('', 'end', text=str(usu.id), values=(usu.dni, usu.nombre, usu.apellido),iid=usu.id)
                else:
                    print("error")

        def grilla(self):
                self.ventana = Toplevel()
                self.ventana.title("Nuevo Socio")
                self.label0 = ttk.Label(self.ventana, text="Nombre: ")
                self.label1 = ttk.Label(self.ventana, text="Apellido:")
                self.label2 = ttk.Label(self.ventana, text="DNI:")
                self.entry0 = ttk.Entry(self.ventana, textvariable=self.Nombre, width=30)
                self.entry1 = ttk.Entry(self.ventana, textvariable=self.Apellido, width=30)
                self.entry2 = ttk.Entry(self.ventana, textvariable=self.Dni, width=30)
                self.boton0 = ttk.Button(self.ventana, text="Agregar", command=self.Agrega)
                self.label0.grid(row=0, column=0)
                self.label1.grid(row=1, column=0)
                self.label2.grid(row=2, column=0)
                self.entry0.grid(row=0, column=1)
                self.entry1.grid(row=1, column=1)
                self.entry2.grid(row=2, column=1)
                self.boton0.grid(row=3, column=2)
#Baja       
        def Baja(self):
                selected_item = self.tree.selection()[0]
                self.CN.baja(selected_item)
                self.tree.delete(selected_item)

#Modificacion
        def Modificar(self):
                x = self.tree.selection()[0]
                print(x)
                for item in x:
                        self.tree.item(item, values=(self.Nombre.get(), self.Apellido.get(), self.Dni.get()))
                        idd = item
                        dni = self.Dni.get()
                        nombre = self.Nombre.get()
                        apellido = self.Apellido.get()
                        print(dni,nombre,apellido)
                socio = Socio(id= idd, dni=dni, nombre=nombre, apellido=apellido)
                print(socio)
                bandera = self.CN.modificacion(socio)
                print(bandera)

                

        def grilla2(self):
                self.ventana = Toplevel()
                self.ventana.title("Nuevo Socio")
                self.label0 = ttk.Label(self.ventana, text="Nombre: ")
                self.label1 = ttk.Label(self.ventana, text="Apellido:")
                self.label2 = ttk.Label(self.ventana, text="DNI:")
                self.entry0 = ttk.Entry(self.ventana, textvariable=self.Nombre, width=30)
                self.entry1 = ttk.Entry(self.ventana, textvariable=self.Apellido, width=30)
                self.entry2 = ttk.Entry(self.ventana, textvariable=self.Dni, width=30)
                self.boton0 = ttk.Button(self.ventana, text="Modificar", command=self.Modificar)
                self.label0.grid(row=0, column=0)
                self.label1.grid(row=1, column=0)
                self.label2.grid(row=2, column=0)
                self.entry0.grid(row=0, column=1)
                self.entry1.grid(row=1, column=1)
                self.entry2.grid(row=2, column=1)
                self.boton0.grid(row=3, column=2)


def main():



    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()
