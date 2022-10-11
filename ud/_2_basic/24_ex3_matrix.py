# Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1], [3, 1, 5]])

import numpy as np

matrix = np.array([[3, 4, 1], [3, 1, 5]])

sum = 0
for line_index in range(matrix.shape[0]):           # shape[0] means quantity of lines 
    for column_index in range(matrix.shape[1]):    # shape[1] means quantity of columns
        sum += matrix[line_index][column_index]

print("Sum: ", sum)