from time import sleep

while True:

    lista = []
    nome = str(input('Digite seu nome completo: '))
    sleep(1)
    sep = nome.split()
    p_nome = sep[0]
    print('Seu primeiro nome é {}'.format(p_nome))
    sobrenome = sep[-1]
    print('Seu sobrenome é {}'.format(sobrenome))
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        lista.append(idade)
        print('Bem Vindo {}, de {} anos!'.format(nome, idade))
    question = str(input('Está correto? [S/N]')).lower()
    if question == 's':
        print('Seja Bem Vindo!')
        lista.append(nome)
        sleep(2)
        print('Lista de usuários:\n{}'.format(lista))
        sleep(2)
    elif question == 'n':
        rep = str(input('Digite seu nome completo: '))
        sleep(2)
        sep = nome.split()
        p_nome = sep[0]
        print('Seu primeiro nome é {}'.format(p_nome))
        sobrenome = sep[-1]
        print('Seu sobrenome é {}'.format(sobrenome))
        lista.append(rep)
        print('Lista de usuários:\n{}'.format(lista))
        sleep(2)
    ask = str(input('Deseja continuar registro? [S/N] ')).lower()
    if ask == 'n':
        print(lista)
        sleep(3)
        break
    
        
    


