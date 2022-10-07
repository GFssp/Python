class Bola:

    def __init__(self, cor, raio):

        self.cor = cor
        self.raio = raio

    def cor(self):

        self.info = self.cor

        return self.info

    def area(self):

        area = 4 * 3.14 * self.raio * self.raio
        self.info = area

        return self.info

    def volume(self):

        volume = 4 * 3.14 * self.raio * self.raio * self.raio/3
        self.info = volume

        return self.info

    def __repr__(self):

        return f'{self.info}'

        
bola1 = Bola('Azul', 5)
print(bola1.area())