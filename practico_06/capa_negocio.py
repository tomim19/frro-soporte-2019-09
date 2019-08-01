# Implementar los metodos de la capa de negocio de socios.
import sys

sys.path.append("C:\SOPORTEV\GIT\practico_05")

from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception): 
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar(id_socio)
         

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return self.datos.buscar_dni(dni_socio)
       
        

    def todoss(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return self.datos.todos()
         

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_1(socio)
            self.regla_2(socio)
            self.regla_3()
            alta = self.datos.alta(socio)
            self.datos.cerrar()
            print(alta)
            if alta == None:
                return False
            else:
                return True
        except DniRepetido:
            print("a")
            return False
        except LongitudInvalida:
            print("b")
            return False
        except MaximoAlcanzado:
            print("c")
            return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """

        bandera = self.datos.baja(id_socio)
        return bandera



    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        try:
            self.regla_2(socio)
        except LongitudInvalida:
            return False
        finally:
            mod = self.datos.modificacion(socio)
            self.datos.cerrar()
            if mod == None:
                return False
            else:
                return True


    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        busq = self.datos.buscar_dni(socio.dni)
        print(busq)
        if busq == False:
            return True
        else:
            raise DniRepetido("Dni repetido")
            

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre)>=self.MIN_CARACTERES) and (len(socio.nombre)<=self.MAX_CARACTERES) and (len(socio.apellido)>=self.MIN_CARACTERES) and (len(socio.apellido)<=self.MAX_CARACTERES):
            return True
        else:
            raise LongitudInvalida("Longitud invalida")
            

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos())==self.MAX_SOCIOS:
            raise MaximoAlcanzado("Maximo de socios alcanzado")
        else:   
            return True

    def cerrar(self):
        self.datos.cerrar()    

       
