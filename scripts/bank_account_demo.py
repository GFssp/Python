# ATRIBUTO DINÂMICO

class Banco(object):

    total = 100000
    reserva = 0.2

    def __init__(self, ID, saldo):

        self.ID = ID
        self.saldo = saldo
    
    def deposito(self, valor):

        self.saldo += valor
    
    def saque(self, valor):

        if self.saldo >= valor:
            self.saldo -= valor


itau = Banco(234, 5000)
itau.deposito(4000)
print(itau.saldo)


# ATRIBUTO ESTÁTICO


class Conta(object):

# Encapsulamento
    __total = 100000
    reserva = 0.2

    def __init__(self, ID, saldo):

        self.ID = ID
        self.saldo = saldo
    
    def deposito(self, valor):

        Conta.__total += valor
        self.saldo += valor
    
    def saque(self, valor):

        if self.saldo >= valor:
            Conta.saldo -= valor
            self.saldo += valor


itau2 = Conta(5467, 5000)
Conta.deposito(itau2, 4000)
print(itau2.saldo)