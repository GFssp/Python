from functools import reduce

# Lambda function
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

print(points2D)
print(points2D_sorted)
print(points2D)
print('-'*20)

# Gera fatorial
a = [2, 3, 4, 5]

product_a = reduce(lambda x, y: x*y, a)
print(product_a)
