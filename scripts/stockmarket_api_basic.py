import requests as rp
from time import sleep


print('--------------------------------------------')
print('STOCK MARKET SOFTWARE - IBM')
print('--------------------------------------------')

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=JZFXHUJIGZW8IS0L'
response = rp.get(url)
dados = response.json()

for data_time in dados['Time Series (5min)']:

    print(f'{data_time} : {dados["Time Series (5min)"][data_time]}')

exit_code = input('Enter para sair')