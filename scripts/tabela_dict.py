from time import sleep

coluna_A = {'Maria': 1, 'Pedro': 0.5, 'João': 3.2}

print(coluna_A)

for k in coluna_A:
    coluna_A['Maria'] = 5
    coluna_A['Pedro'] = 3
    coluna_A['João'] = 1

print(coluna_A)

print(coluna_A['Pedro'])
sleep(2)
