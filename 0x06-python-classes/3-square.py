#!/usr/bin/python3
"""Class Square defines a square"""


class Square:
    """This class defines a square.
    This class has no public attributes.
    """
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
