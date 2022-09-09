#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = []
    new_list = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_length = len(matrix[0])
    for i in matrix:
        if len(i) != matrix_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round((j / div), 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix
