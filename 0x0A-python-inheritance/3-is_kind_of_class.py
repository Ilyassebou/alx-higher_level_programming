#!/usr/bin/python3
"""Contains the is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or if obj is an instance 
    of a class that inherited from, the specified class. """
    return isinstance(obj, a_class)
