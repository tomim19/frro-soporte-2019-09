# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.
import datetime

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla, Peso
from ejercicio_07 import agregar_peso
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import engine
from ejercicio_04 import buscar_persona

Session = sessionmaker(bind=engine)
session = Session()

def listar_pesos(id_persona):
    bandera = buscar_persona(id_persona)
    if bandera is False:
        return  False
    else:
        pes = session.query(Peso).filter(Peso.IdPersona==id_persona).all()
        pesoLista = []
        for p in pes:
            per = (p.Fecha, int(p.Peso))
            pesoLista.append(per)
        return pesoLista


@reset_tabla

def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1).strftime("%Y-%m-%d %S:%M:%S"), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1).strftime("%Y-%m-%d %H:%M:%S"), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [('2018-05-01 00:00:00', 80), ('2018-06-01 00:00:00', 85)]
    assert pesos_juan == pesos_esperados
     #id incorrecto
    assert listar_pesos(200) == False

if __name__ == '__main__':
    pruebas()
session.close()