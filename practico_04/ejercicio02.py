## 2 Ejercicio Hacer un formulario en Tkinter una calculadora que tenga 1 entry y 12 botones para los dígitos 0 al 9
## y las operaciones + - / * = , que al apretar cada botón vaya agregando al valor que muestra en el entry el carácter 
## que le corresponde ( como se ve imagen ) y cuando se aprieta en = pone el resultado de evaluar la cadena entrada . 

from tkinter import *
from tkinter import ttk, font
import getpass



class Aplicacion():
    
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Calculadora 2")

#Variables globales tkinter
        self.operando = StringVar()
        self.resultado = DoubleVar()       
#Texto Entry
        self.ctext1 = ttk.Entry(self.raiz, textvariable=self.operando, width=30 )
#Botones
        self.boton0 = ttk.Button(self.raiz, text="0",
                                 command=self.cero)
        self.boton1 = ttk.Button(self.raiz, text="1",
                                 command=self.uno)
        self.boton2 = ttk.Button(self.raiz, text="2",
                                 command=self.dos)
        self.boton3 = ttk.Button(self.raiz, text="3",
                                 command=self.tres)                         
        self.boton4 = ttk.Button(self.raiz, text="4",
                                 command=self.cuatro)   
        self.boton5 = ttk.Button(self.raiz, text="5",
                                 command=self.cinco)
        self.boton6 = ttk.Button(self.raiz, text="6",
                                 command=self.seis)
        self.boton7 = ttk.Button(self.raiz, text="7",
                                 command=self.siete) 
        self.boton8 = ttk.Button(self.raiz, text="8",
                                 command=self.ocho)   
        self.boton9 = ttk.Button(self.raiz, text="9",
                                 command=self.nueve)
        self.boton10 = ttk.Button(self.raiz, text="+",
                                 command=self.suma)
        self.boton11 = ttk.Button(self.raiz, text="-",
                                 command=self.resta)
        self.boton12 = ttk.Button(self.raiz, text="*",
                                 command=self.multip)
        self.boton13 = ttk.Button(self.raiz, text="%",
                                 command=self.div)
        self.boton14 = ttk.Button(self.raiz, text="=",
                                 command=self.result)
        self.labelvac = ttk.Label(self.raiz, text="")  
        self.labelvac2 = ttk.Label(self.raiz, text="") 
        self.labelvac3 = ttk.Label(self.raiz, text="")                          
#Grilla
        self.ctext1.grid(row=0, column=0, columnspan=20, sticky=NW, padx=5)
        self.labelvac.grid(row=1, column=0)
        self.labelvac2.grid(row=9, column=0)
        self.labelvac3.grid(row=8, column=0)
        self.boton0.grid(row=7, column=0, sticky=W, padx=5)
        self.boton1.grid(row=6, column=0, sticky=W, padx=5)
        self.boton2.grid(row=6, column=1, sticky=W, padx=5)
        self.boton3.grid(row=6, column=2, sticky=W, padx=5)
        self.boton4.grid(row=5, column=0, sticky=W, padx=5)
        self.boton5.grid(row=5, column=1, sticky=W, padx=5)
        self.boton6.grid(row=5, column=2, sticky=W, padx=5)
        self.boton7.grid(row=4, column=0, sticky=W, padx=5)
        self.boton8.grid(row=4, column=1, sticky=W, padx=5)
        self.boton9.grid(row=4, column=2, sticky=W, padx=5)
        self.boton10.grid(row=4, column=3, sticky=W, padx=5)
        self.boton11.grid(row=5, column=3, sticky=W, padx=5)
        self.boton12.grid(row=7, column=3, sticky=W, padx=5)
        self.boton13.grid(row=6, column=3, sticky=W, padx=5)
        self.boton14.grid(row=7, column=1, ipadx=43, columnspan=10, sticky=W, padx=5)
        self.raiz.mainloop()
#BOTON APRETADO    
    def cero(self):
        aux = "0"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def uno(self):
        aux = "1"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def dos(self):
        aux = "2"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def tres(self):
        aux = "3"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def cuatro(self):
        aux = "4"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def cinco(self):
        aux = "5"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def seis(self):
        aux = "6"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def siete(self):
        aux = "7"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def ocho(self):
        aux = "8"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def nueve(self):
        aux = "9"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
    def suma(self):
        aux = "+"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)    
    def resta(self):
        aux = "-"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa) 
    def multip(self):
        aux = "*"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)   
    def div(self):
        aux = "/"
        auxe = self.operando.get()
        auxa = (str(auxe)+aux)
        self.operando.set(auxa)
#RESULTADO
    def result(self):
        self.resultado.set(eval(self.operando.get()))
        print(self.resultado.get()) 

def main():
    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()