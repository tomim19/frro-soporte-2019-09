# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
import sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def buscar_persona(IdPersona):
    sSQL = '''SELECT * FROM Persona WHERE IdPersona=?'''
    c.execute(sSQL, (IdPersona,))
    x = c.fetchone()
    if x is None:
        return False
    else:
        return x


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', '1988-05-15', 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
