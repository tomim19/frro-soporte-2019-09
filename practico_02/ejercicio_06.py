# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import datetime

dt = datetime.now()

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nac = nacimiento

    def edad(self):
        edad = dt.year-self.nac.year
        return int(edad)
d = datetime(1997,2,19)
per = Persona(d)
assert (per.edad()) == 22
