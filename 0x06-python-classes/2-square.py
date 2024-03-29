#!/usr/bin/python3
""" creates class Square """


class Square:
    """class square"""
    def __init__(self, size=0):
        """
        initialize square size

        Args:
        size (int): size of square

        Returns:
        None
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
