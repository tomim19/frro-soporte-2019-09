# Implementar los casos de prueba descriptos.

import unittest
import sys

sys.path.append("C:\SOPORTEV\GIT\practico_05")
from ejercicio_01 import Socio
from ejercicio_02 import DatosSocio
from capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()


    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)
#ESTE HICE
    def test_regla_1(self):
        valido = Socio(dni=1234567, nombre='Roberto', apellido='Suarez')
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)
        

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)
#TODOS ESTOS HICE
    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juannnnnnnnnnnnn', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
                # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
                # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perezzzzzzzzzzzzzzzzzz')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):

        invalido = self.ns.todos>=self.ns.MAX_SOCIOS
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3, invalido)

    def test_baja(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        alta = self.ns.alta(socio)
        #Verifica alta
        self.assertTrue(alta)
        self.assertNotEqual(len(self.ns.todos()), 0)
        baja = self.ns.baja(socio)
        #Verifica baja
        self.assertTrue(baja)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        #Creamos un socio y lo validamos
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        alta = self.ns.alta(socio)
        self.assertTrue(alta)
        self.assertNotEqual(len(self.ns.todos()), 0)

        #Buscamos ese socio
        busq=self.ns.test_buscar(socio)
        self.assertTrue(busq)

    def test_buscar_dni(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        #Creamos un socio y lo validamos
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        alta = self.ns.alta(socio)
        self.assertTrue(alta)
        self.assertNotEqual(len(self.ns.todos()), 0)

        #Buscamos ese socio
        busq=self.ns.test_buscar("12345678")
        self.assertTrue(busq)

    def test_todos(self):
        #Creamos un socio y lo validamos
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        alta = self.ns.alta(socio)
        self.assertTrue(alta)
        #Validamos que todos no devuelva vacio
        self.assertNotEqual(len(self.ns.todos()), [])

    def test_modificacion(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # Alta
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        alta = self.ns.alta(socio)
        #Verifica alta
        self.assertTrue(alta)
        self.assertNotEqual(len(self.ns.todos()), 0)
        socio.nombre = 'Roberto'
        socio.apellido = 'Suarez'
        socio.dni = 1234567
        self.ns.modificacion(socio)
        socio_mod = self.ns.buscar(socio.id)
        
        #Verifica modificacion
        self.assertEqual(socio_mod.id, socio.id)
        self.assertEqual(socio_mod.nombre, 'Roberto')
        self.assertEqual(socio_mod.apellido, 'Suarez')
        self.assertEqual(socio_mod.dni, 13264587)

if __name__ == '__main__':
    ts = TestsNegocio()
    ts.setUp()
    ts.test_alta()
    ts.tearDown()
