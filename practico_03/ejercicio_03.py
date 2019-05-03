# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.


import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Persona, reset_tabla
from ejercicio_02 import agregar_persona

engine = create_engine( 'sqlite:///sqlalchemy_practico03A.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()


def borrar_persona (id_persona): 
    usuario = session.query(Persona).filter(Persona.IdPersona==id_persona).first()
    if usuario is None :
        return False
    else:
        session.delete(usuario)
        session.commit()
        return True
 
@reset_tabla
def pruebas ():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()

session.close()