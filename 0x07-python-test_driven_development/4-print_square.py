#!/usr/bin/python3
""" Defines a function that prints a square using #."""


def print_square(size):
    """Prints a square with the character #
    :arg
        size(int): is the size length of the square
    :raise
        TypeError: if the size isn't integer and
        also size is float and is less than 0.
        ValueError: if the size is not a positive integer
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not (size >= 0):
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
