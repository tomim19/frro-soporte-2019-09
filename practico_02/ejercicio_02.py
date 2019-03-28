# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
from math import pi

class Circulo:

    def __init__(self, radio):
        self.r = radio


    def area(self):
        resultado1 = (self.r**2) *pi
        return resultado1
    def perimetro(self):
        resultado2 = 2* pi * self.r
        return resultado2

C1 = Circulo(3)

print(C1.area())
print(C1.perimetro())

assert(int(C1.area())) == 28
assert(int(C1.perimetro())) == 18
