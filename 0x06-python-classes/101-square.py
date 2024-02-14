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
        """Getter for size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Getter for position."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculate the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square with the '#' character."""
        if self._size == 0:
            print("")
            return

        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

    def __str__(self):
        """String representation of the square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
