# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from practico_03.ejercicio_01 import reset_tabla
from practico_03,ejercicio_01 import Persona


Session = sessionmaker(bind=engine)

def agregar_persona(nombre, nacimiento, dni, altura):
    Base.metadata.sqlalchemy.insert(Persona,)
# import datetime
# import sqlite3
# from practico_03.ejercicio_01 import reset_tabla


# conn = sqlite3.connect('Tabla_Ej1.db')
# c = conn.cursor()

# def agregar_persona (nombre, nacimiento, dni, altura):
#     iSQL='''INSERT INTO Persona (Nombre, FechaNacimiento, DNI, Altura)
#     VALUES (?, ?, ?, ?)'''
#     tdatos= (nombre, nacimiento, dni, altura)
#     c.execute(iSQL, tdatos)
#     conn.commit()
#     id = c.lastrowid
#     return id


# @reset_tabla
# def pruebas():
#     id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
#     id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
#     assert id_juan > 0
#     assert id_marcela > id_juan


# if __name__ == '__main__':
#     pruebas()
