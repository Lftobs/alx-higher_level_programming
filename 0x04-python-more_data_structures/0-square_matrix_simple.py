#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    '''
    using lambda x list comprehension

    new = [list(map(lambda x: x**2, col)) for col in matrix]
    '''
    new = [[i**2 for i in col] for col in matrix]
    return new
