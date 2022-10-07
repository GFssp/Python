import json

info = {'Produto': 'TV', 'Preço': 2.500, 'Parcelamento': 3}
info_data = json.dumps(info)
f = open('teste02.json', 'wb')
f.write(info_data.encode())
f.close()

f = open('teste02.json', 'rb')
data_total = f.readline()
print(data_total.decode())
