from time import sleep

lista = [2, 5, 8, 3, 5]

lista2 = [item*2 for item in lista]
lista_pares = [item for item in lista if item % 2 == 0]

print(f'Lista númerica: {lista2}')
sleep(0.5)
print(f'Lista de pares: {lista_pares}')
sleep(0.5)

lista3 = [numero for numero in range(
    100) if numero % 5 == 0 if numero % 6 == 0]

print(f'De 30 em 30: {lista3}')
sleep(0.5)

print('Substituindo por 1 se o número for divisível por 5, e 0 se não for:')
resultado = [1 if numero % 5 == 0 else 0 for numero in range(16)]
print(resultado)
sleep(2)
