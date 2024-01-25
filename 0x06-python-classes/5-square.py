#!/usr/bin/python3
""" creates class Square """


class Square:
    """ Square class """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Getter method to retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set size """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints the square with the character '#' """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
