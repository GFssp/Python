def conta_letras(string):

    dict = {}
    for letra in string:
        if letra in dict:
            dict[letra] = dict[letra] + 1
        else:
            dict[letra] = 1
    print(dict)


texto = input('Digite algo: ')
conta_letras(texto)
