import math
import numpy

def comb(n,r):
    return math.factorial(n) / ( math.factorial(n-r) * math.factorial(r) )

def binomial(p):
    def f(n, x):
        return comb(n, x) * p**x * (1 - p)**(n - x)
    return f

def poisson(lambd):
    def f(x):
        return float( lambd**x ) * numpy.exp(-lambd) / math.factorial(x)
    return f


