# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla

conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def agregar_peso(id_persona, fecha, peso):
    sSQL='''SELECT * from Persona where IdPersona=?'''
    ttdatos= (id_persona,)
    c.execute(sSQL, ttdatos)
    x = c.fetchone()
    if x is None:
        return False
    else:
        ssSQL='''SELECT * from PersonaPeso where Fecha>? '''
        tttdatos= (fecha,)
        c.execute(ssSQL, tttdatos)
        z = c.fetchone()
        if z is None:
            iSQL='''INSERT INTO PersonaPeso(IdPersona, Fecha, Peso) 
            VALUES(?,?,?)'''
            tdatos= (id_persona, fecha, peso,)
            c.execute(iSQL, tdatos)
            conn.commit()
            id = c.lastrowid
            return id
        else:
            return False






@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
