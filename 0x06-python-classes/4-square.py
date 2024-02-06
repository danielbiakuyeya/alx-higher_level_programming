#!/usr/bin/python3
"""a cass definition of a square"""


class Square(object):
    """square class with private instance attribute"""

    def __init__(self, size=0):
        """Initialization of class instance attribute
        Args:
             size (int): size of the square
            Return: None
        """
        self.size = size

    def area(self):
        """calculate the area square
        Return:
        the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            the value of the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        setter of __size
        Args:
            size (int): the size of the square
        Return: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
