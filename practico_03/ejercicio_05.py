# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
import sqlite3

from Ejercicio1 import reset_tabla
from Ejercicio2 import agregar_persona
from Ejercicio4 import buscar_persona


conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def actualizar_persona(Id_Persona, Nombre2, FechaNacimiento2, DNI2, Altura2):
    c.execute(
        "UPDATE Persona SET  Nombre = ?, FechaNacimiento=?, DNI=?, Altura=? WHERE IdPersona = ?",
        (Nombre2, FechaNacimiento2, DNI2, Altura2, Id_Persona))
    conn.commit()
    cSQL = '''SELECT * FROM Persona WHERE IdPersona=?'''
    c.execute(cSQL, (Id_Persona,))
    aux = c.fetchone()
    if aux is None:
        return False
    else:
        return aux


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.date(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', '1988-04-16', 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.date(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
