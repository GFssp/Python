from itertools import *
from itertools import groupby
from collections import Counter

# Hello World
print('Hello World')


# Texto
print('-'*20)
text = 'hello world'
contagem = Counter(text)
print(contagem)
print('-'*20)

# Sequência numérica
sequel = [2, 8, 6, 4]

# Combinações sem repetição
comb_1 = combinations(sequel, 2)
print(list(comb_1))
print('-'*20)

# Combinações com repetição
comb_2 = combinations_with_replacement(sequel, 2)
print(list(comb_2))
print('-'*20)

# Acumulação
sequel_2 = [2, 7, 9, 1]
acc = accumulate(sequel_2)
print(list(acc))


# Selecionar valores menores que 3
def smaller_than_3(x):
    return x < 3


print('-'*20)
sequel_3 = [2, 6, 1, 9]
group_obj = groupby(sequel_3, key=lambda x: x < 3)
print(list(group_obj))
for key, value in group_obj:
    print(key, list(value))
