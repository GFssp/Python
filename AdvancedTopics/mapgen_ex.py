## Na função gerador map, a lista x não é armazenada

my_list = [5, 2, 4, 1, 9, 5, 2]

x = map(lambda x: x ** 2, my_list)

for n in x:
    print(n)