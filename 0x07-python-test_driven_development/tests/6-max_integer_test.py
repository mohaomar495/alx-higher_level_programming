#!/usr/bin/python3

from unittest import TestCase

max_integer = __import__("6-max_integer").max_integer

class TesMaxInteger(TestCase):
    """Define unittest for max_integer"""

    def testOrderedList(self):
        """Test ordered list"""
        ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(max_integer(ordered_list), 10)

    def testUnorderedList(self):
        """Test unordered list """
        unorderedList = [2, 3, 5, 1, 0, 10, 9, 7, 8, 4]
        self.assertEqual(max_integer(unorderedList), 10)

    def testOrderedFloat(self):
        """ Test ordered float list"""
        orderedFloatList =  [1.1, 2.2, 4.6, 8.9]
        self.assertEqual(max_integer(orderedFloatList), 8.9)

    def testUnorderedFloatList(self):
        """ Test unordered float list """
        unorderedFloatList = [6.7, 1.1, 4.3, 9.2]
        self.assertEqual(max_integer(unorderedFloatList), 9.2)

    def testSingleInteger(self):
        """ Test list containing one single integr """
        singleContainingIntegerList = [5]
        self.assertEqual(max_integer(singleContainingIntegerList), 5)

    def testSingleFloat(self):
        """ Test list containing one single float number """
        singleContainingFloatList = [5.5]
        self.assertEqual(max_integer(singleContainingFloatList), 5.5)

    def testCharacterContainingList(self):
        """ Test charchter containing lists """
        charContainingList = ["a", "B", "r", "R"]
        self.assertEqual(max_integer(charContainingList), "r")

    def testStringContainingList(self):
        """ Test string containing lists """
        strContainingList = ["Hello", "Mohammad", "name", "base"]
        self.assertEqual(max_integer(strContainingList), "name")

    def testEmptyList(self):
        """ Test empty list """
        emptyList = []
        self.assertEqual(max_integer(emptyList), None)
