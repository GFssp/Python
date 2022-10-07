def repeat(get_string):

    # args e kwargs são obrigatórios pois tanto a função start quando a função my_other_string
    # precisariam de parametros caso args e kwargs não existissem
    def start(*args, **kwargs):
        print("Aleluia!")
        value = get_string(*args, **kwargs)
        return value
    
    return start

@repeat
def my_string(x):
    return x

@repeat
def my_other_string():
    print("Heya!")


my_string('Boa!')
my_other_string()
