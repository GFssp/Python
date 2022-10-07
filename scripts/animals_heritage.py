class Mamífero:

    def __init__(self, cor_de_pelos, genero, andar):
        
        self.cor_de_pelos = cor_de_pelos
        self.genero = genero
        self.num_patas = andar

    def falar(self):
        print('Olá, sou mamífero e sei falar!')

    def andar(self):
        print(f'Estou andando sobre {self.num_patas} patas')

    def amamentar(self):
        if self.genero.lower()[0] == 'm':

            print('Machos não amamentam')
            return
        
        print('Amamentando meu filhote')

class Pessoa(Mamífero):

    def __init__(self, cor_de_pelos, genero, andar):
        super().__init__(cor_de_pelos, genero, andar)

    def falar(self):
        super(Pessoa, self).falar()
        print('Olá, sou uma pessoa e sei falar')