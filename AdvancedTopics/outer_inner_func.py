def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)

    # Sem parentesis, a função abaixo não executa nada
    # Mas é possível captura o valor de dentro dela
    return inner_func


# a variável my_func passa a ser uma função com a mesma funcionalidade da função outer_func
my_func = outer_func()
my_func()