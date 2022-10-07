from time import sleep

class Ball:

    def __init__(self, cor, raio):

        self.cor = cor
        self.raio = raio

    def cor(self):

        return self.cor

    def area(self):

        area = 4 * 3.14 * self.raio * self.raio
        return area

    def volume(self):

        volume = 4 * 3.14 * self.raio * self.raio * self.raio/3
        return volume

b = Ball('azul', 5)
print(f'Raio: {b.raio}')
print(f'Área: {b.area()}')
print(f'Volume: {b.volume()}')
sleep(3)





