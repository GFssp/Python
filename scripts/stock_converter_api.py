import requests as rp
from time import sleep

url = "https://v6.exchangerate-api.com/v6/71bf4ecfe1105f8833e29d88/latest/USD"
res = rp.get(url)

dados = res.json()
dados['base_code'] = 'EUR'

v_euro = dados['conversion_rates']['EUR']
v_libra = dados['conversion_rates']['GBP'] 

print(f'{v_euro} Euros - {v_libra} Libras')
euros = float(input('Informe o valor em Euros para ver seu valor em libras: '))

print('{} euros equivalem a {:.2f} libras atualmente'.format(euros, euros / v_euro))
sleep(2)