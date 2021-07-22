#!/usr/bin/env python3
"""defines a function to sumate a square"""


def summation_i_squared(n):
    """get the series of a squared sequence"""
    if type(n) not in [int, float] or n < 0:
        return None
    if n == 0:
        return 0
    else:
        return summation_i_squared(n-1) + n*n
