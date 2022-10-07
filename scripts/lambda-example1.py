def build_quadratic_funtion(a, b, c):
    return lambda x: a*x**2 + b*x + c

my_function = lambda x: 3*x + 1
f = build_quadratic_funtion(2, 3, -5)


quadratic_result = f(2)
my_function_result = my_function(5)

print(quadratic_result + my_function_result)
