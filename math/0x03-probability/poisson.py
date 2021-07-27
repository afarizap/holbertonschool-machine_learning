#!/usr/bin/env python3
""" poisson task """


class Poisson():
    """represents a poisson distribution"""
    def __init__(self, data=None, lambtha=1.):
        """initialize values"""
        if data is not None:
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            if type(data) is not list:
                raise TypeError("data must be a list")
            # Promedio
            lambtha = sum(data)/len(data)
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        self.lambtha = float(lambtha)
