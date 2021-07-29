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
        if data == None:
            if n < 0 and type(n) is not int:
                raise ValueError("n must be a positive value")
            if p < 0 or 1 < p:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            n = len(data)/2 #calcular
            p = len([i for i in data if i > n]) #calcular

        self.n = int(n)
        self.p = float(p)