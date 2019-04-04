# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
from practico_02.ejercicio_03 import Persona
"""
from datetime import datetime
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
        """print("Nombre:",self.n)
        print("Edad:",self.e)
        print("Sexo:",self.s)
        print("Peso:",self.p)
        print("Altura:",self.a)
        print("Documento:",self.dni)"""

"""
class Estudiante (Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self,"Tomas",22,"hombre",70,1.70)
        self.carre=carrera
        self.an=anio
        self.mate=cantidad_materias
        self.apro=cantidad_aprobadas

    def avance(self):
        porcen=(self.apro/self.mate)*100
        return porcen


    # implementar usando modulo datetime
    def edad_ingreso(self):
        dt = datetime.now()
        aux = dt.year-self.an
        edadin = self.e-aux
        return edadin

est = Estudiante ("Sistemas",2015,20,5)

assert(est.avance() == 25.0)
assert(est.edad_ingreso() == 18)
