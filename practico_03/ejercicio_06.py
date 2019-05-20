# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from ejercicio_01 import borrar_Tabla, crear_Tabla, Persona
from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy import create_engine

Base=declarative_base()

class Peso(Base):
        __tablename__ = 'PersonaPeso'
        IdPeso = Column(Integer, primary_key=True, autoincrement=True)
        IdPersona = Column(Integer, ForeignKey(Persona.IdPersona))
        Fecha = Column(String)
        Peso = Column(Float)

def crear_Tabla_Peso():
        Peso.__table__.create()

def borrar_Tabla_Peso():
        Peso.__table__.drop()

engine=create_engine( 'sqlite:///sqlalchemy_practico03A.db',echo=True)
Base.metadata.bind = engine

 # no modificar
def reset_tabla(func):
        def func_wrapper():
                crear_Tabla()
                crear_Tabla_Peso()
                func()
                borrar_Tabla_Peso()
                borrar_Tabla()
        return func_wrapper
