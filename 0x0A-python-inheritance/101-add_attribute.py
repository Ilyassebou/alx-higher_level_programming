#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_attribute(obj, name, value):
    """Method checking if attribute can be set and sets
    where possible"""
    try:
        setattr(obj, name, value)
    except AttributeError:
        raise TypeError("can't add new attribute")

