## 1 Ejercicio Hacer un formulario tkinter que es una calculadora, tiene 2 entry para ingresar los valores V1 y V2.
## Y 4 botones de operaciones para las operaciones respectivas + , - , * , / ,
## al cliquearlos muestre el resultado de aplicar el operador respectivo en los V1 y V2 . 

from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (pack)

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Calculadora")
#VARIABLES
        self.operando1 = DoubleVar()
        self.operando2 = DoubleVar()
        self.total = DoubleVar()
#LABELS        
        self.etiq1 = ttk.Label(self.raiz, text="Primer operando:")
        self.etiq2 = ttk.Label(self.raiz, text="Segundo operando:")
        self.etiq3 = ttk.Label(self.raiz, text="")
#ENTRYS
        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.operando1, 
                                width=30)
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.operando2, 
                                width=30) 
#BOTONES  
        self.boton3 = ttk.Button(self.raiz, text="+",
                                 command=self.suma)
        self.boton4 = ttk.Button(self.raiz, text="-",
                                 command=self.resta)                         
        self.boton5 = ttk.Button(self.raiz, text="x",
                                 command=self.multip)   
        self.boton6 = ttk.Button(self.raiz, text="%",
                                 command=self.div) 
#GRILLA    
        self.etiq1.grid(row=0 , column=0)
        self.etiq2.grid(row=0 , column=1) 
        self.etiq3.grid(row=3, column=0)                        
        self.ctext1.grid(row=1 , column=0)                    
        self.ctext2.grid(row=1 , column=1, padx=20)
        self.boton3.grid(row=1 , column=3, padx=5)
        self.boton4.grid(row=1 , column=4, padx=5)
        self.boton5.grid(row=1 , column=5, padx=5)
        self.boton6.grid(row=1 , column=6, padx=5) 
        
        self.raiz.mainloop()
#FUNCIONES
    def grilla2(self, opera):
        self.ventana = Toplevel()
        self.ventana.title(opera)
        self.etiq1 = ttk.Label(self.ventana, text="Resultado:")
        self.etiq2 = ttk.Label(self.ventana, textvariable=self.total)
        self.etiq3 = ttk.Label(self.ventana, text="")
        self.etiq4 = ttk.Label(self.ventana, text="                                                  ")
        self.etiq1.grid(row=0 ,column=0, sticky=W)
        self.etiq2.grid(row=0, column=2, padx=5, sticky=W)
        self.etiq3.grid(row=1, column=0)
        self.etiq4.grid(row=0, column=5, columnspan=5)

    def suma(self):
        op1 = float(self.operando1.get())
        op2 = float(self.operando2.get())
        resultado = op1 + op2
        self.total.set(resultado)
        self.grilla2("Suma")                  
        
    def resta(self):
        op1 = float(self.operando1.get())
        op2 = float(self.operando2.get())
        resultado = op1 - op2
        self.total.set(resultado)
        self.grilla2("Resta")                    
       
    def multip(self):
        op1 = float(self.operando1.get())
        op2 = float(self.operando2.get())
        resultado = op1 * op2
        self.total.set(resultado)
        self.grilla2("Multiplicacion")                  
       
    def div(self):
        op1 = float(self.operando1.get())
        op2 = float(self.operando2.get())
        resultado = op1 / op2
        self.total.set(resultado)
        self.grilla2("Division")
              
def main():
    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()