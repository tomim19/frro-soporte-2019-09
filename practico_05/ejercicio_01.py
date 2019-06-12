# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer)
    nombre = Column(String(250))
    apellido = Column(String(250))


engine = create_engine('sqlite:///socios.db')
Base.metadata.bind = engine


def crear_Tabla():
    Socio.__table__.create()

def borrar_Tabla():
    Socio.__table__.drop()

def reset_tabla(func):
    def func_wrapper():
        crear_Tabla()
        func()
        borrar_Tabla()
    return func_wrapper
