#!/usr/bin/python3
"""a class definition for Square"""


class Square(object):
    """defines a Square
    Attributes:
        __size(int): size of the square
    """
    def __init__(self, size):
        """Initializes to Square Instances
        Args:
            size: size of the square
        """
        self.__size = size
