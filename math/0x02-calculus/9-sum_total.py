#!/usr/bin/env python3
"""defines a function to sumate a square"""


def summation_i_squared(n):
    """get the series of a squared sequence"""
    if not str(n).isnumeric() or n < 1:
        return None
    if n == 1:
        return 1
    else:
        return summation_i_squared(n-1) + n * n
