import json

class User:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


print('Estabelecendo base de dados em JSON...')
user = ('John', 45)


def enconde_user(o):
    if isinstance(o, User):
        return {'nome': o.nome, 'idade': o.idade, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')


usuário_JSON = json.dumps(user, default=enconde_user)
print(usuário_JSON)
