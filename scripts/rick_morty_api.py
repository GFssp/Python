import requests as rp
from selenium import webdriver
from time import sleep


pagina = int(input('Digite o número relativo a página de personagens [0 a 35]: '))
print(f'Personagens da Página {pagina}:')

url = f'https://rickandmortyapi.com/api/character?page={pagina}'
response = rp.get(url)
dados = response.json()
#driver = webdriver.Chrome("C:/Users/jose marcos/Documents/Let's Code 2/Requests_API/chromedriver.exe")

lista_personagens = [print('->', dado['name']) for dado in dados['results']]

nome_id = int(input('Informe o número do personagem para ver informações [0 até 671]: '))

if nome_id > 0 and nome_id < 671:

    url = f'https://rickandmortyapi.com/api/character/{nome_id}'
    response = rp.get(url)
    dados = response.json()

    for k, v in dados.items():
        print(f'{k}: {v}')
    
    sleep(10)

else:

    print('Número inválido')


        
