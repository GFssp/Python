class Retangulo:

    def __init__(self, lado_a, lado_b):

        self.a = lado_a
        self.b = lado_b

    def area(self):

        self.area = self.a * self.b
        return self.area

    def __repr__(self):

        return f'Resultado: {self.a * self.b}'


r = Retangulo(5, 2)
print(r)