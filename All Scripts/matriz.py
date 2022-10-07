import numpy as np
from random import random

# Version 1
def cria_matriz(num_linhas, num_colunas, valor):
    matriz_inicial = []
    for i in range(num_linhas):
        linha = [] 
        for j in range(num_colunas):
            linha.append(valor)

        matriz_inicial.append(linha)
    
    for l in matriz_inicial:
        print(l)

# Version 2
def generate_empty_matrix(lines_n, columns_n):
    try:
        new_matrix = np.zeros((lines_n, columns_n))
        return new_matrix
    except Exception as e:
        return e

new = generate_empty_matrix(2, 3)
print(new)