#!/usr/bin/python3

""" Square class """


class Square:

    """Square"""

    def __init__(self, size=0):
        """
        Initializes the size of square

        args:
            size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
