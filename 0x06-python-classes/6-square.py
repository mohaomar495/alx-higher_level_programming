#!/usr/bin/python3

"""
Square Class
"""


class Square:
    """
    Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size of the square

        :arg size(int): size of the square as integer

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        getters

        :return: size(int)
        """
        return self.__size

    @size.setter
    def size(self, value):
        """

        :param value(int): new value of the size paramater
        :return: size(int)
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """
        position getter
        :return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter
        :param value(tuple -> int): takes tuple of 2 positive integers
        :return: tuple
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all((num >= 0) for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Area

        :return: area(int) of the square
        """
        return self.__size**2

    def my_print(self):
        """
        display the square as #
        :return: square as #
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
