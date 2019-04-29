# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3

conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()

def crear_tabla_peso():
    c.execute(
        '''CREATE TABLE IF NOT EXISTS PersonaPeso(IdPersona INTEGER, Fecha DATE, Peso INTEGER, FOREIGN KEY ("IdPersona") REFERENCES "Persona"("IdPersona")) ''')



def borrar_tabla_peso():
    c.execute('''DROP TABLE PersonaPeso''')



# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
