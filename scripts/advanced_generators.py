# Generetors are functions that return a object that an iterated over, and they generate the objects
# inside easyly
from time import sleep
# Adicionando valores para a função por meio do metódo yield


def my_generator_1():
    yield 1
    yield 2
    yield 3


# Função para adicionar linhas
def line():
    print('--'*20)


g = my_generator_1()

# Metódo "Next" para mostrar o primeiro valor criado na função
line()
print('Primeiro valor gerado na função:')
value = next(g)
print(value)
line()

# Para cada item na função, é mostrado um valor
line()
print('Valores numéricos criados na função "Generator":')
for i in g:
    sleep(1)
    print(i)
line()
sleep(1)


# Função para diminuir a contagem usando a outra função "yield"
def countdown(num):
    print('Starting counting...')
    while num > 0:
        yield num
        num -= 1


cd = countdown(4)

value_2 = next(cd)
print(value_2)
sleep(1)
print(next(cd))
sleep(1)
print(next(cd))
sleep(1)
print(next(cd))
sleep(1)
line()


# Gerar valores de 0 até um número especificado


def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


# Substituto com a função yield

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print('Soma de valores de 0 até 100')
print(sum(firstn_generator(100)))
line()


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


print('Sequência de fibonacci para valores de 0 à 30...')
fib = fibonacci(30)
for i in fib:
    print(i, end=sleep(1))
