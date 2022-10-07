from random import choice

def baralho():

    cartas = ['Ás', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Q', 'J', 'K']
    print('Baralho Criado!')
    return cartas

def jogador():

    pontuacao = 0
    return pontuacao

def jogada(nome):
    
    pontuacao = jogador()
    comprar = input(f'{nome}, Deseja comprar uma carta? ').lower()
    if comprar == 'sim':
        carta_al = sorteio()
        print(pontuacao)
        if carta_al == 'Ás':
            carta_al = 1
            pontuacao += carta_al
        elif carta_al == 'Q':
            carta_al = 10
            pontuacao += carta_al
        elif carta_al == 'J':
            carta_al = 10
            pontuacao += carta_al
        elif carta_al == 'K':
            pontuacao += carta_al
            carta_al = 10 
    elif comprar == 'não':
        pontuacao += carta_al
        print(f'Suas cartas somam {pontuacao}')

def sorteio():
    carta_al = baralho()
    return choice(carta_al)

def verificacao():
    pontuacao = jogador()
    if pontuacao == 21:
        print(f'Parabéns! Você venceu {nome}')
    elif pontuacao > 21:
        print(f'Você perdeu {nome}!')

def main():

    n_jogadores = int(input('Quantos jogadores vão jogar: '))
    for jogador in range(n_jogadores):
        nome = input('Informe o nome: ')
    baralho()
    jogada(nome)
    verificacao()


main()
