import pickle

arq = open('Lista de Frutas.pck', 'wb')
frutas = ['maça', 'banana', 'pera', 'uva']
f_string = pickle.dump(frutas, arq)
arq.close()

arq = open('Lista de Frutas.pck', 'rb')
data = pickle.load(arq)
print(data)