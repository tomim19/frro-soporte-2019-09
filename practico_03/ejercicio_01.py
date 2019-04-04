# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


import sqlite3

conn = sqlite3.connect('Tabla_Ej1.db')
c = conn.cursor()
def crear_tabla():
    c.execute('''CREATE TABLE Persona(IdPersona INTEGER PRIMARY KEY AUTOINCREMENT, Nombre TEXT, FechaNacimiento TEXT,DNI INTEGER, Altura INTEGER) ''')


def borrar_tabla():
    c.execute('''DROP TABLE Persona''')


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
