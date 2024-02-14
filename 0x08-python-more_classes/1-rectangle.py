#!/usr/bin/python3
"""A class that defines a rectangle by:
    (based on 0-rectangle.py)
"""


class Rectangle:
    """Define the class for the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter property for self.width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """setter property for self.width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter/setter property for self.height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

