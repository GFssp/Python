import collections
from collections import Counter

c = Counter('guilherme')
print(c)
a = Counter(['a', 'a', 'b', 'c', 'd', 'd'])
print(a)
b = Counter({'a': 1, 'b': 2})
z = Counter(cats=4, dogs=7)

# Retorna 0 ao invés de um erro 
# Como o que acontece em dicionários
print(z['pet'])

# o 4 e 7 passa a ser a quantidade de vezes que as palavras dogs and cats aparecem na lista
print(list(z.elements()))

# Os dois elementos mais comuns 
print(a.most_common(2))

