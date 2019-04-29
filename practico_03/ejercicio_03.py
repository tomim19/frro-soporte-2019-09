# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3
from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def borrar_persona (id_persona):
    sSQL = '''SELECT * FROM Persona WHERE IdPersona=?'''
    c.execute(sSQL, (id_persona,))
    aux = c.fetchone()
    if aux is None:
        return False
    else:
        dSQL='''DELETE FROM Persona WHERE IdPersona=?'''
        c.execute(dSQL, (id_persona,))
        conn.commit()
        return True



@reset_tabla
def pruebas ():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
