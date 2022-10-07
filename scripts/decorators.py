import functools


def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        return result
        print('End')
    return wrapper


@start_end_decorator
def add5(x):
    return x + 5


result = add5(10)
print(result)
print('Decorators tornam possível criar funções dentro de outras funções')
print('-'*20)


def repeat_sentence(num_times):
    def decorator_repeat(func_2):
        @functools.wraps(func_2)
        def wrapper_2(*args, **kwargs):
            for _ in range(num_times):
                result = func_2(*args, **kwargs)
            return result
        return wrapper_2
    return decorator_repeat


@repeat_sentence(1)
def greet(name):
    print(f'Welcome to python {name}!')


global nome
nome = str(input('Type your name: '))
greet(nome)
print('-'*20)


class CountCalls:

    def __init__(self, func_3):
        self.func_3 = func_3
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This was executed {self.num_calls} time(s)')
        return self.func_3(*args, **kwargs)


@CountCalls
def say_hello():
    print('Hello')


say_hello()
print('-'*20)
