# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.b = base
        self.a = altura

    def area(self):
        resultado =self.b*self.a
        return resultado
    
R1 = Rectangulo(20,30)


assert(R1.area()) == 600
