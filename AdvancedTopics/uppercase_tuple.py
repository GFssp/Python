class UppercaseTuple(tuple):

    """o metodo especial new permite alterar os valores antes de serem inicializados"""
    def __new__(cls, iterable):
        upper_iterable = (word.upper() for word in iterable)
        return super().__new__(cls, upper_iterable)


print(UppercaseTuple(['banana', 'phone', 'clever']))