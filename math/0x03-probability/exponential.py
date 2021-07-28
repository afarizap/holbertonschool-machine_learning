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

    def pdf(self, x):
        """ Calculates the value of the PDF (probability density function)
            for a given time period
            x: Time period
        """
        if x < 0:
            return 0
        e = 2.7182818285
        PDF = (self.lambtha * (e ** (-self.lambtha * x)))
        return PDF

    def cdf(self, x):
        """ Calculates the value of the CDF (cumulative distribution function)
            for a given time period
            x: Time period
        """
        if x < 0:
            return 0
        e = 2.7182818285
        CDF = (1 - (e ** (-self.lambtha * x)))
        return CDF
