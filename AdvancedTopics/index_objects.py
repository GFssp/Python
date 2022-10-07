""" POO Avançado I: Objetos Indexáveis """

class MinhaLista(object):

    # O objeto da classe recebe o tamanho como parâmetro
    def __init__(self, tamanho):
        self.len = tamanho

    # Permite iterar sobre o objeto da classe
    def __getitem__(self, index):
        if index < self.len:
            return index ** 2
        else:
            raise StopIteration

class ListaMultipla(object):

    # O objeto da classe recebe valores como parâmetros e os adiciona em uma lista
    def __init__(self, *args):
        self.data = []
        for arg in args:
            self.data.append(arg)

    # Permite iterar sobre o objeto da classe
    def __getitem__(self, index):
        return self.data[index]**2

class SlicedList:

    # Determina se o valor passado como parametro é um inteiro ou um slicing
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

class SequenciaAritimetica:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.modificado = {} 
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                raise IndexError 
            # O bloco dentro do try só roda quando há uma alteração de valores (__setitem__)
            try:
                return self.modificado[index]  
            #--------------------------------
            except KeyError:
                return self.start + index * self.step
        
        else:
            if index.step == None:
                step = 1
            else:
                step = index.step

            # Armazena o intervalo numerico em uma lista
            data = []
            for i in range(index.start, index.stop, step):
                data.append(self[i])
            return data
    
    # Metodo usado em caso de alteração de valor
    # exemplo: t[2] = 5 
    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError
        self.modificado[index] = value 

class SequenciaAritimetica2:
    def __init__(self, start=0, end=1, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.data = list(range(start, end, step))
        self.modificado = {}

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                raise IndexError
            try:
                return self.modificado[index]
            except KeyError:
                return self.data[index]
        
        else:
            return self.data[index]
    
    def __delitem__(self, index):
        del self.data[index]

            

lista = MinhaLista(5)
m_lista = ListaMultipla(0, 1, 2, 3, 4)
s_lista = SlicedList()
s = SequenciaAritimetica(1, 5)
s2 = SequenciaAritimetica2(1, 6, 2)

""" 
for item in lista:
    print(item)

for item in m_lista:
    print(item) 

s_lista[0: 5: 2]

print(s[5]) -- __getitem__
print(s[2: 7]) -- __getitem__
s[4] = 2 -- __setitem__

print(s2[2])
"""
