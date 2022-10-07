import requests as rp
from random import randint

url = f"http://numbersapi.com/{}/{}/date"
res = rp.get(url)

dados = res.text
print(dados)