class ContaCorrente:

    def __init__(self, saldo, cliente):

        self.cliente = cliente
        self.saldo = saldo

    def realizar_depósito(self):

        self.maxim = 100000
        dep = float(input('Quanto deseja depositar? '))
        if dep < self.maxim:
            self.saldo += dep
            print(f'Saldo atual: {self.saldo}')
        else:
            print('Valor muito alto para depósito')

    def realizar_saque(self):

        saque = float(input('Quanto deseja sacar? '))
        if saque <= self.saldo:
            self.novo_saldo = self.saldo - saque
            print('{} reais resgatados com sucesso!'.format(saque))
            print('Novo saldo: {}'.format(self.novo_saldo))
        else:
            print('Saldo não suficiente')

    def realizar_transferência(self):

        trans = float(input('Quanto deseja transferir? '))
        if trans < self.maxim:
            print('{} reais transferidos com sucesso!')
        else:
            print('Valor muito alto para realizar transferência')

class ContaVip(ContaCorrente):

    def __init__(self, saldo, cliente, cheque_especial):

        super().__init__(saldo, cliente)
        self.cheque_especial = cheque_especial

    def depositar_cheque(self):

        self.maxim = 1000000
        self.saldo += self.cheque_especial
        print(f'Saldo Atual: {self.saldo}')


cliente1 = ContaVip(500000, 'Guilherme', 300000)
cliente1.realizar_depósito()
cliente1.depositar_cheque()