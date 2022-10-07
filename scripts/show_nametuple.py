from databases import registros
from pprint import pprint

registros = [
    registros(nome="John", idade=20, nacionalidade="American")
]

pprint(registros)

for info in registros[0]:
    print(info)

print(registros[0].nome)
