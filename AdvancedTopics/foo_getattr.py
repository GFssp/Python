class Foo(object):

    def __getattr__(self, attr):
        print("looking up", attr)
        value = 42
        self.__dict__[attr] = value
        return value

    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item) 

f = Foo()
print(f.current)