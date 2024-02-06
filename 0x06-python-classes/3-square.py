#!/usr/bin/python3
"""a class definition of a square"""


class Square(object):
    """square class with private instance attribute"""

    def __init__(self, size=0):
        """Initialization of class instance attribute
        Args:
            size (int): size of the square
            Return: None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area square
        Return:
        the area of the square
        """
        return self.__size ** 2
