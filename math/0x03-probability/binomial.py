#!/usr/bin/env python3
""" binomial task """


class Binomial():
    """represents a binomial distribution"""
    def __init__(self, data=None, n=1, p=0.5):
        """ Initialize Binomial
            Args:
            data: list of the data used to estimate the distribution
            n: number of Bernoulli trials
            p: probability of a “success”
        """
        if data is None:
            if n < 0 and type(n) is not int:
                raise ValueError("n must be a positive value")
            if p < 0 or 1 < p:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            variance = 0
            mean = sum(data) / len(data)
            for i in data:
                variance += (i-mean) ** 2
            variance /= len(data)
            q = variance / mean
            p = 1 - q
            n = round(mean / p)
            p = mean / n
        self.n = int(n)
        self.p = float(p)
