
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
        self.dni = self.generar_dni()
        self.print_data()
    def es_mayor_edad(self):
        if (self.e >= 18):
            esmayor = True
        else:
            esmayor = False
        return esmayor

    # llamarlo desde __init__
    def generar_dni(self):
        doc = randint(10000000,99999999)
        return doc

    def print_data(self):
        print("Nombre:",self.n)
        print("Edad:",self.e)
        print("Sexo:",self.s)
        print("Peso:",self.p)
        print("Altura:",self.a)
        print("Documento:",self.dni)

p1 = Persona("Tomas",22,"hombre",70,1.70)
print("Mayor de edad?",p1.es_mayor_edad())

assert(p1.es_mayor_edad()) == True


