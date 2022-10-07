from time import sleep

tupla = (1, 2, 3, 5, 'sete', 11.0)

print(f'Primeiro número da tupla: {tupla[0]}')

print('Percorrendo a tupla...')
for elemento in tupla:
    print(elemento)

lista = list(tupla)

lista.append(13)
print(lista)

tuplanova = tuple(lista)
print(tuplanova)
sleep(2)
