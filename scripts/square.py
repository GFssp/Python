class Retangulo:

    def __init__(self, lado_a, lado_b):

        self.a = lado_a
        self.b = lado_b

    def area(self):

        area = self.a * self.b
        return f'Área: {area}'

class Quadrado(Retangulo):

    def __init__(self, lado_a, lado_b):

        super().__init__(lado_a, lado_b)
        
        if self.a != self.b:
            print('A figura não é um quadrao')
    
    def area(self):

        area = self.a * self.b
        return f'Área: {area}'

quadrado1 = Quadrado(5, 5)
print(quadrado1.area())
