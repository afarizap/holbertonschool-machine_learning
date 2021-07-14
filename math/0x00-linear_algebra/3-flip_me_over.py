#!/usr/bin/env python3
""" Flip Me Over  """


def matrix_transpose(matrix):
    """ returns transpose of a 2D matrix """
    return list(map(list, (zip(*matrix))))
