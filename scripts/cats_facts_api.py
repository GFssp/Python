import requests as rp
import json
from time import sleep

print('--------------------------------------------------------')
print('WELCOME TO CAT FACTS API')
print('--------------------------------------------------------')
digit = int(input('Type a number to see a cat description: '))
url = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={digit}'
response = rp.get(url)
dados = response.json()

print(dados[0]['text'])
sleep(5)
