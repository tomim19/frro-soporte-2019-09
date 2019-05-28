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
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el  
        # módulo 'font' al comienzo del programa):
        
        fuente = font.Font(weight='bold')
        
        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior: 
                               
        self.etiq1 = ttk.Label(self.raiz, text="Primer operando:", 
                               font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Segundo operando:", 
                               font=fuente)
        
        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña: 
        
        self.operando1 = IntVar()
        self.operando2 = IntVar()
        
        # Realiza una lectura del nombre de usuario que 
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # información se ha importando el módulo getpass
        # al comienzo del programa):
        
        self.operando1.set(getpass.getuser())
        
        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del
        # programa quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" (asterisco) para ocultar la 
        # escritura de las contraseñas:
        
        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.operando1, 
                                width=30)
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.operando2, 
                                width=30)
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:
        
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", 
                                 command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", 
                                 command=quit)
        self.boton3 = ttk.Button(self.raiz, text="+",
                                 command=self.suma)
        self.boton4 = ttk.Button(self.raiz, text="-",
                                 command=self.resta)                         
        self.boton5 = ttk.Button(self.raiz, text="x",
                                 command=self.multip)   
        self.boton6 = ttk.Button(self.raiz, text="/",
                                 command=self.div)                                               
        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando 
        # hacia el lado de arriba, excepto, los dos últimos, 
        # los botones, que se situarán debajo del último 'TOP':
        # el primer botón hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opción 'side' son: 
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor será TOP
        # La opción 'fill' se utiliza para indicar al gestor
        # cómo expandir/reducir el widget si la ventana cambia
        # de tamaño. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e 
        # Y (Verticalmente). Funcionará si el valor de la opción
        # 'expand' es True.
        # Por último, las opciones 'padx' y 'pady' se utilizan
        # para añadir espacio extra externo horizontal y/o 
        # vertical a los widgets para separarlos entre sí y de 
        # los bordes de la ventana. Hay otras equivalentes que
        # añaden espacio extra interno: 'ipàdx' y 'ipady':
                                         
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton3.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton4.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton5.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton6.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:
                
        self.ctext2.focus_set()
        
        self.raiz.mainloop()
    
    # El método 'aceptar' se emplea para validar la 
    # contraseña introducida. Será llamado cuando se 
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores 
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.
    
    def aceptar(self):
            print("Operando1:   ", self.ctext1.get())
            print("Operando2:", self.ctext2.get())
            self.operando1.set("")
            self.operando2.set("")
            self.ctext2.focus_set()
    def suma(self):
        resultado = self.operando1 + self.operando2
        return resultado
    def resta(self):
        resultado = self.operando1 - self.operando2
        return resultado
    def multip(self):
        resultado = self.operando1 * self.operando2
        return resultado
    def div(self):
        resultado = self.operando1 % self.operando2
        return resultado

def main():
    mi_app = Aplicacion()
    return mi_app

if __name__ == '__main__':
    main()