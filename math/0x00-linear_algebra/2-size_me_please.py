#!/usr/bin/env python3
""" function that returns a matrix shape """


def matrix_shape(matrix):
    """ Calculates the shape of a matrix """
    return list(array(matrix).shape)

if __name__ == "__main__":
    from numpy import array