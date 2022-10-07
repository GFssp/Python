class Data:

    def __init__(self, dia, mes, ano):

        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __eq__(self, other):

        return self.dia == other.dia

    def __gt__(self, other):

        return self.dia > other.dia

    def __ge__(self, other):

        return self.dia >= other.dia

    def __lt__(self, other):

        return self.dia < other.dia

    def __le__(self, other):

        return self.dia <= other.dia

    def __ne__(self, other):

        return self.dia != self.dia

    def __repr__(self):

        return f'{self.dia}/{self.mes}/{self.ano}'
    
hoje = Data(16, 1, 2020)
amanhã = Data(17, 1, 2020)

diferenca = hoje < amanhã

print(diferenca)