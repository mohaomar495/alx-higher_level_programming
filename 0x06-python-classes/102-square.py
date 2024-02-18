#!/usr/bin/python3

""" class Square """


class Square:
    """Square"""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int, or float): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size**2

    def __eq__(self, other):
        """
        Determines if the area of one square is
        equal to the area of another square.

         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current
            square is equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Determines if the area of one square is
        not equal to the area of another square.

         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current
            square is not equal to, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Determines if the area of one square is
        greater than the area of another square.

         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current
            square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Determines if the area of one square is greater
        than or equal the area of another square.
         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current
            square is greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Determines if the area of one square is
        less than the area of another square.

         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current
            square is less than, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Determines if the area of one square is less than
        or equal the area of another square.
         Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the current square
            is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
