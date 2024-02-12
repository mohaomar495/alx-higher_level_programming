#!/usr/bin/python3

"""
Square Class
"""


class Square:
    """
    Square
    """

    def __init__(self, size):
        """
        Initializes the size of the square

        :arg size(int): size of the square as integer

        """
        self.__size = size

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
        self.__size = value

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

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
