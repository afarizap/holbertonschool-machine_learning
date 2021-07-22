#!/usr/bin/env python3
"""defines a function to sumate a square"""


def summation_i_squared(n):
    """get the series of a squared sequence"""
    if type(n) not in [int]:
        return None
    return int((n * (n+1) * (2*n + 1)) / 6)
