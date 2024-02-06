#!/usr/bin/python3
"""class definition of a square"""


class Square(object):
    """square class with private instance attribute"""

    def __init__(self, size=0):
        """Initialization of class instance attribute
        Args:
            size (int): size of the square
            Return: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
