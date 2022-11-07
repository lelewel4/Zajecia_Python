import numpy as np

def sub_matrix(matrix:list[int], column:int):
    sub_matrix = matrix[:]
    sub_matrix = np.delete(sub_matrix, 0, axis=0)               #delete row
    sub_matrix = np.delete(sub_matrix, column, axis = 1)        #delete column
    return sub_matrix

def matrix_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        det = 0
        for col in range(len(matrix[0])):
            sign = (-1) ** (0 + col)
            det += sign * matrix[0][col] * matrix_determinant(sub_matrix(matrix, 0, col))
    return det

