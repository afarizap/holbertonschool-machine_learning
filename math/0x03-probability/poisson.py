#!/usr/bin/env python3
""" poisson task """


class Poisson():
    """represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """initialize values"""
        # self.data = data
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if data is not None:
        #     # Promedio
        #     lambtha = sum(data)/len(data)
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
        # self.lambtha = float(lambtha)
