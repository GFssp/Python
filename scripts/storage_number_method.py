from time import sleep

def apresentação():
    print('Bem Vindo ao Python')
    num = int(input('Digite um número para ser armazenado: '))
    return num


def armazena():
    lista_numeros = []
    lista_numeros.append(apresentação())
    print(lista_numeros)
    sleep(2)

def main():
    armazena()

main()

