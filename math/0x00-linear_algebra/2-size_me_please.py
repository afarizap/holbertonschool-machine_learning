#!/usr/bin/env python3
from numpy import array
""" function that returns a matrix shape """


def matrix_shape(matrix):
    """ Calculates the shape of a matrix """
    return list(array(matrix).shape)
