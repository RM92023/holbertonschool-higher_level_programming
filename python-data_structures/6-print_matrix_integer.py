#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col, element in enumerate(row):
            print('{:d}'.format(element), end='')
            if col != len(row)-1:
                print(' ', end='')
        print()
