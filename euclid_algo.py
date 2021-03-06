
from math import remainder


def gcd(x, y):
    """
    Euclid Algorithm used for computing the greated common denominator
    Args:
        x (int): an integer variable
        y (int): an integer variable
    """
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller
    if(remainder == 0):
        return(smaller)

    if(remainder != 0):
        return(gcd(smaller, remainder))

print(gcd(81,18))