#!/usr/bin/python3
"""a Square class blue print"""


class Square(object):
    """square class with private instance attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of class instance attribute"""
        self.size = size
        self.position = position

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2

    @property
    def position(self):
        """Getter of position"""
        return self.__position

    @position.setter
    def position(self, position):
        """Setter of position"""
        if (len(position) != 2 or
                type(position) is not tuple or
                not all(isinstance(num, int) for num in position) or
                not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Getter of size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter of size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        """Print out the square"""
        if self.size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.size):
                    print("#", end="")
                print("")

    def __str__(self):
        """Define how __str__ should print the square"""
        if self.__size != 0:
            [print("") for n in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for i in range(0, self.__position[0])]
                [print("#", end="") for j in range(0, self.__size)]
                if i != self.__size - 1:
                    print("")
        return ""
