#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for array in range(len(matrix)):
            for position in range(len(matrix)):
                print("{}".format(matrix[array][position]), end='')
            print(end="\n")
        return
    else:
        print(end="\n")
