# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



Base = declarative_base() 
class Persona(Base):
    __tablename__ = "Persona" 
    IdPersona = Column(Integer, primary_key=True, autoincrement=True)
    Nombre = Column(String)
    FechaNacimiento = Column(String)
    DNI = Column(Integer)
    Altura = Column(Integer)

engine = create_engine( 'sqlite:///sqlalchemy_practico03A.db',echo=True)
Base.metadata.bind = engine


def crear_Tabla():
    Persona.__table__.create()

def borrar_Tabla():
    Persona.__table__.drop()

def reset_tabla(func):
    def func_wrapper():
        crear_Tabla()
        func()
        borrar_Tabla()
    return func_wrapper
