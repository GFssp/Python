from time import sleep

class Retangulo:

    def __init__(self, lado_a, lado_b):

        self.a = lado_a
        self.b = lado_b

    def area(self):

        return self.a * self.b

retangulo = Retangulo(8, 5)
print(f'Área do Retângulo: {retangulo.area()}')
sleep(2)
