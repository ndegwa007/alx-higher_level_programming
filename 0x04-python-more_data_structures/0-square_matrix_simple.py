#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    k = []
    for i in range(len(matrix)):
        k.append(list(map(lambda a: a * a, matrix[i])))
    return k
