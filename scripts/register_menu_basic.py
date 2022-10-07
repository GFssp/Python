users = {}
dados = {}
soma = 0

while True:

    print('''[1] - Cadastrar novo usuário
    [2] - Imprimir usuários cadastrados
    [3] - Encerrar
    [4] - Buscar CPF''')
    pergunta = int(input('O que deseja fazer? '))
    if pergunta == 1:
        cpf = int(input('Informe o CPF: '))
        nome = input('Informe o nome para cadastro: ')
        idade = int(input('Informe a idade: '))
        email = input('Informe o email: ')
        dados['Nome'] = nome
        dados['Idade'] = idade
        dados['Email'] = email
        users[cpf] = dados
        print('Usuário cadastrado com sucesso!')
    if pergunta == 2:
        print('Clientes Cadastrados: ')
        print(users)
    if pergunta == 3:
        print('Programa encerrado')
        break
    if pergunta == 4:
        busc_cpf = int(input('Informe o cpf para ver os dados do usuário: '))
        if busc_cpf in users.keys():
            pessoa = users[busc_cpf]
            print(pessoa)
        else:
            print('Nenhum usuário encontrado!')


