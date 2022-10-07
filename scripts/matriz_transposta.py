from time import sleep

transposta = []
matriz = [[2, 6, 8, 3],
          [5, 9, 2, 1],
          [10, 4, 7, 0]]

print('Matriz: ')
for linha in matriz:

    print(linha)
sleep(1)

transposta = [[linha[i] for linha in matriz] for i in range(4)]

print('Matriz transposta: ')
for linha in transposta:

    print(linha)

sleep(1)
res = input('Sair? ')
if 'n' in res:
    sleep(10)
