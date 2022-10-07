import requests as rq

class Cidade:

    def __init__(self, nome, temp_max, temp_min, umidade, descricao, ultima_atualizacao):

        self.nome = nome
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.umidade = umidade
        self.descricao = descricao
        self.ultima_atualizacao = ultima_atualizacao
        
        api_key = "5d0b33a3adaa365fb1561a27d2baade8"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.nome}&appid={api_key}&units=metric&lang=pt_br"
        resposta = rq.get(url)

        self.dados = resposta.json()

    def temp_max(self):

        self.temp_max = self.dados['main']['temp_max']
        
        return self.temp_max

    def temp_min(self):

        self.temp_min = self.dados['main']['temp_min']

        return self.temp_min

    def umidade(self):

        self.umidade = self.dados['main']['umidade']

        return self.umidade

    def descricao(self):

        self.descricao = self.dados['weather']['description']

        return self.descricao

    def __repr__(self):

        print(f'{self.temp_max}/{self.temp_min}/{self.umidade}/{self.descricao}')




        
