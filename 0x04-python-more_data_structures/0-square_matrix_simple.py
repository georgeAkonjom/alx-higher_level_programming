#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    one_d = [[elem**2 for elem in row] for row in matrix]
    return(one_d)
