#!/usr/bin/env python3
"""integrate"""


def poly_integral(poly, C=0):
    """calculates the integral of a polynomial"""
    if type(poly) != list or type(C) != int:
        return None
    new = []
    for i in range(1, len(poly) + 1):
        new += [poly[i-1]/i]
    new.insert(0, C)
    return new