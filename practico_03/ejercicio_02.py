# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Persona, reset_tabla, engine 

Session = sessionmaker(bind=engine)
session = Session()

def agregar_persona(nombre, nacimiento, dni, altura):    
    persona = Persona()
    persona.Nombre = nombre
    persona.FechaNacimiento = nacimiento
    persona.DNI = dni
    persona.Altura = altura 
    session.add(persona)
    session.commit()
    return persona.IdPersona

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.date(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.date(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()

session.close()