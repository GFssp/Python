import requests as rq
from random import randint

num_al = randint(1, 10000)
url = f"http://numbersapi.com/{num_al}/math"

res = rq.get(url)

dados = res.text
print(dados)