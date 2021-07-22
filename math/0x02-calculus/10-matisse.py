#!/usr/bin/env python3
"""defines a function for derivative pol"""


def poly_derivative(poly):
    """calculates derivative of poly"""
    if type(poly) != list or len(poly) == 0:
        return None
    new = []
    n = 0
    for i in poly:
        new += [i * n]
        n += 1
    if new[1:] == []:
        return [0]
    return new[1:]
