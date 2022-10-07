import requests as rp
from random import randint

num_al = randint(1, 10000)
url = f"http://numbersapi.com/{num_al}"
res = rp.get(url)

dados = res.text
print(dados)