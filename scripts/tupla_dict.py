from time import sleep

lista_idades = []
lista_nomes = []

perfis = {'Guilherme': 18, 'Raquel': 16,
          'Davi': 18, 'Matheus': 23, 'Gabriel': 25}

print(f'Perfis:\n{perfis}')
print('--'*10)
sleep(2)

for v in perfis:

    idades = perfis[v]
    lista_idades.append(idades)

for k in perfis.keys():

    nomes = k
    lista_nomes.append(nomes)

print(f'Lista de idades: \n{lista_idades}')
print('--'*10)
sleep(2)
print(f'Lista de nomes: \n{lista_nomes}')
print('--'*10)
sleep(2)
