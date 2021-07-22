#!/usr/bin/env python3
"""defines a function to sumate a square"""


def summation_i_squared(n):
    """get the series of a squared sequence"""
    r = 0
    for i in range(1, n + 1):
        r += i ** 2
    return r
