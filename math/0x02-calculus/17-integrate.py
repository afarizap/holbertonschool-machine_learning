#!/usr/bin/env python3
"""integrate"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""
    if type(poly) != list or type(C) != int or len(poly) == 0:
        return None
    new = [C]
    i = 1
    for n in poly:
        r = n/i
        i += 1
        if r - int(r) == 0:
            r = int(r)
        new += [r]
        while new[-1] == 0:
            new.pop()
    return new
