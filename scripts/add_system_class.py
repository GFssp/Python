class Cliente:

    def __init__(self, nome, cpf):

        self.nome = nome
        self.cpf = cpf
    
    def __repr__(self):
        
        return f'{self.nome}, {self.cpf}'

class Sistema:

    def __init__(self, clientes = []):

        clientes = []
        self.clientes = clientes

    def adicionar_cliente(self, novo_cliente):

        self.clientes.append(novo_cliente)
        print(self.clientes)

sistema = Sistema

cliente1 = Cliente('Guilherme', 97723491)
Sistema().adicionar_cliente(cliente1)
