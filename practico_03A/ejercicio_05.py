# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from ejercicio_01 import Base, Persona, reset_tabla, engine
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona

Session = sessionmaker(bind=engine)
session = Session()

def actualizar_persona(Id_Persona, Nombre2, FechaNacimiento2, DNI2, Altura2):
    bandera = buscar_persona(Id_Persona)
    if bandera is False:
        return False
    else:
        actualizar = update(Persona).where(Persona.IdPersona == Id_Persona).values(Nombre=Nombre2,FechaNacimiento=FechaNacimiento2,DNI=DNI2,Altura=Altura2)
        session.execute(actualizar)
        session.commit()

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (1, 'juan carlos perez', datetime.datetime(1988, 4, 16).strftime("%Y-%m-%d %H:%M:%S"), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()
session.close()