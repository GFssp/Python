class Dono_de_caes:
    
    def __init__(self, nome, idade, cao):

        self.nome = nome
        self.idade = idade 
        self.cao = cao

    def treinar(self):

        self.cao.Da_patinha()
        self.cao.latir()

class Cachorro:

    def __init__(self, nome, cor):

        self.nome = nome
        self.cor = cor

    def Da_patinha(self):

        print(f'{self.nome} estendeu a patinha')

    def latir(self):

        print('AUAUAUAUAUAUAUA')

rex = Cachorro('Rex', 'marrom')
pedro = Dono_de_caes('Pedro', 24, rex)

print(pedro.cao.cor)




