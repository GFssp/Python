class Sistema:

    cadastrados = 0

    def __init__(self):

        self.ativado = True
        self.cont = 0
        cadastros = {}
        self.cadastros = cadastros

    def cadastrar_cliente(self, nome, idade, email, cpf):

        self.nome = nome
        self.idade = idade
        self.email = email
        self.cpf = cpf

        lista.append(self.nome)
        lista.append(self.idade)
        lista.append(self.cpf)

        self.cadastros[self.cpf] = lista
        print('Cliente Cadastrado com sucesso')
        Sistema.cadastrados = Sistema.cadastrados + 1
        self.cont += 1
        print('-'*10)
        print(self.cadastros)

    def alterar_cadastro(self):

        self.nome = input('Informe o nome: ')
        self.idade = int(input('Informe a idade: '))
        self.email = input('Informe o email: ')

        self.cpf = input('Informe o CPF: ')

        lista[0] = self.nome
        lista[1] = self.idade
        lista[2] = self.email

        self.cadastros[self.cpf] = lista
    
        print('Cadastro alterado com sucesso!')
        print('-'*10)
        print(self.cadastros)

    def imprimir_cadastros(self):

        print('Cadastros: ', self.cadastros)

    def sair(self):

        self.ativado = False
        pass

lista = []

while True:

    ask = int(input('''    [1] - Cadastrar Cliente
    [2] - Alterar Cadastros
    [3] - Sair
    O que deseja fazer?  '''))

    if ask == 1:
        
        nome = input('Informe o nome: ')
        idade = int(input('Informe a idade: '))
        email = input('Informe o email: ')
        cpf = input('Informe o CPF: ')
        Sistema().cadastrar_cliente(nome, idade, email, cpf)
        print('-'*10)
        ask2 = input('Deseja sair: ').lower()
        if ask2 == 'sim':
            break

    elif ask == 2:

        Sistema().alterar_cadastro()
        ask3 = input('Deseja sair: ').lower()
        if ask3 == 'sim':
            break

    elif ask == 3:

        print('Cadastro Finalizado.')
        break

        


