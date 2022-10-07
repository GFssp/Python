class Financeiro:

    def __init__(self, saldo, imposto_mensal, salario, gastos):

        self.saldo = saldo
        self.imposo_mensal = imposto_mensal
        self.salario = salario
        self.gastos = gastos
    

    def __add__(self, outra):
        self.saldo += outra.saldo
        return self.saldo
        
    def __sub__(self, outra_conta):
        self.saldo -= outra_conta.saldo
        return self.saldo
    
    def __str__(self):
        return f'Saldo: {self.saldo}\nImposto Mensal: {self.imposo_mensal}'


    
conta = Financeiro(25000, 500, 2500, 300)

