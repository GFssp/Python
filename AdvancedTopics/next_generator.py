class Gen():

    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration()
        
        rv = self.last ** 2
        self.last += 1
        return rv

def alt_gen(n):
    for i in range(n):
        # Generator
        yield i ** 2

# Do the same thing
s1 = Gen(100)
s2 = alt_gen(100)

while True:
    try:
        print(next(s1))
    except StopIteration:
        break

for i in s2:
    print(i)