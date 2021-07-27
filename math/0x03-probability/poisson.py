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
        e = 2.7182818285
        factorial = 1
        try:
            for _ in range(1, k + 1):
                factorial *= _
        except e:
            return 0
        PMF = ((self.lambtha ** k) * (e ** -self.lambtha)) / factorial
        return PMF
