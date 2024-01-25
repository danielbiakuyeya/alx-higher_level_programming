#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = matrix[:]
    new_matrix = []
    for row in copy_matrix:
        temp = [x * x for x in row]
        new_matrix.append(temp)
    return (new_matrix)
