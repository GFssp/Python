def cria_classe(**args):
    return type('minhaClasse', (object, ), args)

a = cria_classe(idade = 13, altura = 1.78)
print(a.idade)