#!/usr/bin/env python3
""" poisson task """


class Poisson():
    """represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """initialize values"""
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Promedio
            lambtha = sum(data)/len(data)
        self.data = data
        self.lambtha = float(lambtha)

    def pmf(self, k):
        """ Calculates the value of the PMF(probability mass function)
            for a given number (k)
        """
        if type(k) is not int:
            k = int(k)
        if k < 0:
            return 0
        e = 2.7182818285
        factorial = k
        for i in range(1, k):
            factorial *= i
        return ((self.lambtha ** k) * (e ** -self.lambtha)) / factorial
         
