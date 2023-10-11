#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    M = matrix.copy()
    for i in range(len(matrix)):
        M[i] = list(map(lambda j: j ** 2, matrix[i]))
    return M
