class TestList:

    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.modificado = {} # ?
    
    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0:
                raise IndexError
            try:
                return self.modificado[index] 
            except KeyError:
                return self.start + index * self.step
        else:
            if index.step == None:
                step = 1
            else:
                step = index.step

            data = []
            for i in range(index.start, index.stop, step):
                data.append(self[i])
            return data, self.modificado

    def __setitem__(self, index, value):
        if index < 0:
            raise IndexError
        self.modificado[index] = value

t = TestList(2, 5)
t[2] = 12
print(t[1:4])