def conta_itens(lista):

    dict = {}
    for letra in lista:
        if letra in dict:
            dict[letra] = dict[letra] + 1
        else:
            dict[letra] = 1
    print(lista)
    print(dict)


lista = ['maçã', 'bola', 'arvore']
conta_itens(lista)
