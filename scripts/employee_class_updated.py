from time import sleep

class Funcionario:

    def __init__(self, nome, email):
        
        self.nome = nome
        self.email = email

        dict_horas = {'Janeiro': 240, 'Fevereiro': 240, 'Março': 240,
        'Abril': 240, 'Maio': 240, 'Junho': 240, 'Julho': 240, 'Agosto': 240,
        'Setembro': 240, 'Outubro': 240, 'Novembro': 240, 'Dezembro': 240}

        dict_salario = {'Janeiro': 20, 'Fevereiro': 20, 'Março': 20,
        'Abril': 25, 'Maio': 20, 'Junho': 20, 'Julho': 20, 'Agosto': 20,
        'Setembro': 20, 'Outubro': 20, 'Novembro': 20, 'Dezembro': 20}

        self.dict_h = dict_horas
        self.dict_s = dict_salario

    def salario_mensal(self):

        for hora in self.dict_h.values():
            for salario in self.dict_s.values():
                return salario * hora

func1 = Funcionario('João', 'joão@gmail.com')        
print(func1.salario_mensal())
sleep(2)


