import json

data = {'Nome': 'John', 'Idade': 20, 'Peso': 70, 'Altura': 1.80}

data_string  = json.dumps(data)
file = open('teste.json', 'wb')
file.write(data_string.encode())
file.close()
