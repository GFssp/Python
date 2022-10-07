'''A solução é utilizar o operador * - que, neste caso, não será uma multiplicação. Ao colocarmos o * 
ao lado do nome de um parâmetro na definição da função, estamos dizendo que aquele argumento será uma coleção. 
Mais especificamente, uma tupla. Porém, o usuário não irá passar uma tupla. Ele irá passar quantos argumentos 
ele quiser, e o Python automaticamente criará uma tupla com eles.

O exemplo abaixo cria uma função de somatório que pode receber uma quantidade arbitrária de números.'''


def somatorio(*numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma


s1 = somatorio(5, 3, 1)
s2 = somatorio(2, 4, 6, 8, 10)
s3 = somatorio(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(s1, s2, s3)
