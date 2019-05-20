# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.


import datetime

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla, Peso
from ejercicio_04 import buscar_persona
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import engine


Session = sessionmaker(bind=engine)
session = Session()

def buscar_peso(id_persona,fecha):
    bandera = session.query(Peso).filter(Peso.IdPersona==id_persona, Peso.Fecha > fecha).first()
    if (bandera is None):
        return False
    else:
        return True

def agregar_peso(id_persona, fecha, peso):
    bandera = buscar_persona(id_persona)
    if bandera is False:
        return False
    else:
        Pes = buscar_peso(id_persona,fecha)
        if Pes is True:
            return False
        else:
            Pe = Peso()
            Pe.IdPersona=id_persona
            Pe.Fecha=fecha
            Pe.Peso=peso
            session.add(Pe)
            session.commit()
            return Pe.IdPersona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 30), 85)

if __name__ == '__main__':
    pruebas()
session.close()