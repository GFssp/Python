from time import sleep

class Cliente:

    def __init__(self, nome, idade, email):

        self.nome = nome
        self.idade = idade
        self.email = email
        
    def mostrar_info(self):
    
        print('Nome:', self.nome)
        print('\n')
        print('Idade:', self.idade)
        print('\n')
        print('Email:', self.email)
