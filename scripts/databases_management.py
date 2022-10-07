from collections import namedtuple

registros = namedtuple('Registro', [
    "nome",
    "idade",
    "nacionalidade",
])

# Criando registros
guilherme = registros(nome="Guilherme", idade=20, nacionalidade="Brasileiro")



