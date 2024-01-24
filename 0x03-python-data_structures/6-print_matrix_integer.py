#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mtx in matrix:
        for n in mtx:
            print("{:d}".format(n), end=" " if n != mtx[-1] else "")
        print()
