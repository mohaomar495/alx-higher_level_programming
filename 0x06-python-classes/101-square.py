#!/usr/bin/python3

""" class Square """

class Square:
    """Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getters
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter
        args:
            value(int): the new value for the size of the square
        return: updated size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size**2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Display str representation"""
        if self.__size != 0:
            [print("") for i in range(self.__position[1])]
        for j in range(self.__size):
            [print(" ", end="") for n in range(self.__position[0])]
            [print("#", end="") for m in range(self.__size)]
            if i != self.__size - 1:
                print("")
        return ""
