# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from Ejercicio2 import agregar_persona
from Ejercicio6 import reset_tabla
from Ejercicio7 import agregar_peso

conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def listar_pesos(id_persona):
    sSQL='''SELECT * FROM Persona WHERE IdPersona=?'''
    tdatos= (id_persona,)
    c.execute(sSQL, tdatos)
    x= c.fetchone()
    if x is None:
        return False
    else:
        ssSQL='''SELECT Fecha, Peso FROM PersonaPeso WHERE IdPersona=?'''
        ttdatos= (id_persona,)
        c.execute(ssSQL, ttdatos)
        lista=c.fetchall()
        return lista



@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.date(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.date(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
