# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base() #--- clase padre para definir las tablas
class Persona(Base):
    __tablename__ = 'Persona' #--- indispensable.
    IdPersona = Column(Integer, primary_key=True, autoincrement=True) #--- indispensable
    Nombre = Column(String)
    FechaNacimiento = Column(DateTime)
    DNI = Column(Integer)
    Altura = Column(Integer)

engine = create_engine( 'sqlite:///sqlalchemy_ejemplo0.db',echo=True)
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def crear_Tabla():
    Base.metadata.create_all(engine)

def borrar_Tabla():
    Base.metadata.delete_all(engine)

def reset_tabla(func):
    def func_wrapper():
        crear_Tabla()
        func()
        borrar_Tabla()
    return func_wrapper