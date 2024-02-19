#!/usr/bin/python3

"""
Function for addition of two numbers.
"""

def add_integer(a, b=98):
    """
    function that adds two integer or floats and returns the added values.

    :param a: must be an integer or float
    :param b: must be an integer or float
    :return: returns an integer which is the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return round(a + b)
