class Register:

    def __init__(self, rlist=None):

        self.rlist = rlist
        if isinstance(self.rlist, type(None)):
            self.rlist = []

    def create_user(self, name, age, phone_number, email):

        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.email = email

        self.user = (self.name, self.age, self.phone_number, self.email)

        if not self.age <= 18:

            print('Usuário registrado com Sucesso!')
            self.rlist.append(self.user)

        else:

            print('Falha ao Registrar Usuário: Idade inválida.')

        return self.user


def get_config():

    user_list = []

    r = Register([]).create_user(
        args.nome, args.idade, args.celular, args.email)

    user_list.append(r)
    now = datetime.datetime.now()

    return f'{user_list}\n{now}'


def main():

    print(get_config())


if __name__ == '__main__':
    import argparse
    import datetime
    import sqlite3

    parser = argparse.ArgumentParser(
        description='Registre um novo usuário ao Banco de Dados!')
    parser.add_argument('-n', '--nome', type=str, metavar='',
                        required=True, help='Digite um nome')
    parser.add_argument('-i', '--idade', type=int,
                        metavar='', required=True, help='Digite uma idade')
    parser.add_argument('-c', '--celular', type=int,
                        metavar='', required=True, help='Digite um telefone celular')
    parser.add_argument('-e', '--email',
                        metavar='', required=True, help='Digite um email')
    args = parser.parse_args()

    main()
