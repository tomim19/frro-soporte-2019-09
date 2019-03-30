# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.


from practico_02.ejercicio_04 import Estudiante
"""
from random import randint
from datetime import datetime


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
"""


est1 = Estudiante ("Sistemas",2015,20,5)
est2 = Estudiante ("Civil",2015,20,5)
est3 = Estudiante ("Sistemas",2015,20,5)
est4 = Estudiante ("Mecanica",2015,20,5)
est5 = Estudiante ("Civil",2015,20,5)
listaestudiantes = [est1,est2,est3,est4,est5]


def organizar_estudiantes(estudiantes):
        estudiantesxcarrera = {}
        n = 0
        for i in estudiantes:
            if (estudiantes[n].carre in estudiantesxcarrera) is True:
                valor = estudiantesxcarrera.get(estudiantes[n].carre)
                incremento = valor + 1
                estudiantesxcarrera.update({estudiantes[n].carre : incremento})
            else:
                estudiantesxcarrera.update({estudiantes[n].carre:1})
            n = n + 1
        return estudiantesxcarrera

print (organizar_estudiantes(listaestudiantes))

assert(organizar_estudiantes(listaestudiantes)) == {'Sistemas': 2, 'Civil': 2, 'Mecanica': 1}
