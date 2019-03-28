
# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
from random import randint

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.n = nombre
        self.e = edad
        self.s = sexo
        self.p = peso
        self.a = altura
        self.dni = generar_dni()
        print_data()
    def es_mayor_edad(self):
        if (self.e >= 18):
            esmayor = True
        else:
            esmayor = False
        return esmayor

    # llamarlo desde __init__
    def generar_dni(self):
        doc =[]
        for i in range (0,7):
            append.doc = randint(0,9)

    def print_data(self):
        print(self.n)
        print(self.e)
        print(self.s)
        print(self.p)
        print(self.a)
        print(self.dni)


