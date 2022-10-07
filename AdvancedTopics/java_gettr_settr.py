""" POO Avançado V: Propriedades e Descritores """

class Pessoa(object):
    def __init__(self, nome):
        # Underscore: o atributo passa a ficar sujeito aos metodos abaixo
        self._nome = nome
    def getNome(self):
        print('Obtendo...')
        return self._nome
    def setNome(self, valor):
        print('Modificando...')
        self._nome = valor
    def delNome(self):
        print('Removendo...')
        del self._name
    
    # A propriedade property permite que não seja necessario chamar os metodos diretamente abaixo
    nome = property(getNome, setNome, delNome, "Documentação da propriedade nome")

bob = Pessoa('Bob Smith')
print(bob.nome)
bob.nome = 'Robert Smith'
print(bob.nome)
print('-'*20)
sue = Pessoa('Sue Jones')
print(sue.nome)
print(Pessoa.nome.__doc__)
