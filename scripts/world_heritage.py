from time import sleep

class Planeta():

    def __init__(self):

        self.mundo = 'Terra' 
    
    def Pousar(self):

        print(f'Você acaba de pousar na {self.mundo}! Bem Vindo!')

    def Desviar(self):

        print('Até Mais!')


class Oceano(Planeta):

    def __init__(self, oceano):

        self.oceano = oceano
        print(f'Você acaba de pousar em algum lugar do oceano {self.oceano}...')
        
        

class Continente(Planeta):

    def __init__(self, continente):

        self.continente = continente
        print(f'Pelos dados analisados, você nota que está em algum lugar da {self.continente}...')
        
    
class País(Continente):
    
    def __init__(self, país):

        self.país = país
        print(f' Você está no(a) {self.país}!')
        


def main():
    terra = Planeta()
    terra.Pousar()
    sleep(1.5)
    c = Continente('Ásia')
    sleep(1.5)
    p = País('China')
    sleep(1.5)
        

if __name__ == '__main__':
    main()
