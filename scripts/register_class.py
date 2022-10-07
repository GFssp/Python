class register:

    def __init__(self, nome, idade, altura, peso):

        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def get_array(self):

        rdict = {}
        rdict['Nome'] = self.nome
        rdict['Idade'] = self.idade
        rdict['Altura'] = self.altura
        rdict['Peso'] = self.peso
        return rdict







