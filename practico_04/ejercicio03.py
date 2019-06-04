## 3 Ejercicio Crear un Formulario que usando el control Treeview muestre la una lista con los nombre de
## Ciudades Argentinas y su código postal ( por lo menos 5 ciudades ) . 

from tkinter import *
from tkinter import ttk


class Aplicacion():

    def __init__(self):
        raiz = Tk()
        tree = ttk.Treeview(raiz)
#Columnas
        tree["columns"]=("one","two")
        tree.column("#0", width=100)
        tree.column("one", width=100 )
        tree.column("two", width=100)
        tree.heading("#0", text="Id")
        tree.heading("one", text="Ciudad")
        tree.heading("two", text="Codigo Postal")
#Insert
        tree.insert("" , 0,    text="id", values=("Rosario","2000"))
        tree.insert("" , 1,    text="id", values=("Santa Fe","3000"))
        tree.insert("" , 2,    text="id", values=("Arroyo Seco","2128"))
        tree.insert("" , 3,    text="id", values=("Villa Constitucion","2919"))
        tree.insert("" , 4,    text="id", values=("Rafaela","2300"))
#Loop
        tree.pack()
        raiz.mainloop()

def main():
    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()