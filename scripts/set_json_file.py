import json

# Dict para objeto Json
carros_dict = {'marca': 'honda', 'modelo': 'HRV', 'cor': 'prata'}

carros_list = ['honda', 'volksvagem', 'ford', 'fiat', 'chevrolet']

carros_tuple = ('honda', 'volksvagem', 'ford', 'fiat', 'chevrolet')

carros_j = json.dumps(carros_list, indent=4, separators=(':', ' = '), )

print(carros_j)
