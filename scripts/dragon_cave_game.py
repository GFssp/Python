import random
from time import sleep

def suspense():
    print('Você se aproxima da caverna...')
    sleep(1)
    print('Está escuro e assustador...')
    sleep(1)
    print('Um grande dragão pula na sua frente, ele abre a boca e...')
    print()
    sleep(1)


print('-=' * 20)
print('{:^37}'.format('CAVERNA DO DRAGÃO'))
print('-=' * 20)
print('''Você está perdido em uma ilha cheia de dragões. A sua frente, há duas cavernas,
Uma possui um dragão amigável que dividirá o ouro encontrado com você, porém existe outro dragão feroz 
e faminto que te comerá ao se aproximar de você.''')
print('-=' * 20)
friendlycave = random.randint(1, 2)
escolha = int(input('Qual caverna você escolhe, a 1 ou a 2? '))
if escolha == friendlycave:
    suspense()
    print('Entrega para você o tesouro!')
else:
    suspense()
    print('Ele te devora!')
    print('-='* 20)
input('Enter para sair')



