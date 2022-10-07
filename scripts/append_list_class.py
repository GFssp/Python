import time

class MinhaLista(object):

    def __init__(self, *args):
        self.data = []
        for arg in args:
            self.data.append(arg)

    def __getitem__(self, index):
        return self.data[index]**2

seq = MinhaLista(2, 5, 7, 2)
for i in seq:
    print(i)
