#!/usr/bin/env python3
""" function that returns a matrix shape """


def matrix_shape(matrix):
    """ Calculates the shape of a matrix """
    shape = []
    while type(matrix) == list:
        shape += [len(matrix)]
        matrix = matrix[0]
    return shape
