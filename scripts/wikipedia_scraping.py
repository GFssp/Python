import requests as rq
from bs4 import BeautifulSoup
from time import sleep

url = 'https://pt.wikipedia.org/wiki/Python'
resposta = rq.get(url)

if resposta.status_code == 200:
    site = BeautifulSoup(resposta.content, 'html.parser')

    # Buscando elementos h1 (primeiro parágrafo do site)
    h1 = site.find('h1')
    print(h1.get_text())

    p = site.find('p')
    descricao = p.get_text()
    print(descricao)

    spans = site.find_all('span', class_='mw-headline')
    spans = spans[:-4]
    secoes = []
    for span in spans:
        secoes.append(span.get_text())

    print(f'Título: {h1}')
    print(f'Descrição: {descricao}')
    print('Tópicos: ')
    for topico in secoes:
        print(topico)
