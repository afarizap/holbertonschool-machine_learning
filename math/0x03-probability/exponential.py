#!/usr/bin/env python3
""" exponential task """


class Exponential:
    """ represents an exponential distribution """

    def __init__(self, data=None, lambtha=1.):
        """ class constructor """
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        if data is not None:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Promedio
            lambtha = len(data)/sum(data)
        self.data = data
        self.lambtha = float(lambtha)
