# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.


from practico_02.ejercicio_04 import Estudiante


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
