#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        power = list(map(lambda x : x**2, row))
        new_matrix.append(power)
    return new_matrix
        
