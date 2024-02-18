#!/usr/bin/python3

""" MagicClass """

from math import pi

class MagicClass:
    """ circle. """

    def __init__(self, radius=0):
        """
        initialize a MagicClass.

        args:
            radois (int, or float): the radius of the ciorcle.
        """
        self.__radius = 0

        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ return the area of the circle. """
        return self.__radius ** 2 * pi

    def circumference(self):
        """ returns the circumference of the circle """
        return 2 * self.__radius * pi
