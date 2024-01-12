#!/usr/bin/python3
"""define matrix divided by number """


def matrix_divided(matrix, div):
    if type(matrix) != list and all(isinstance(row, list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    ret = []
    for row in matrix:
        re = []
        for i in row:
            r = round(i / div, 2)
            re.append(r)
        ret.append(re)
    return ret
