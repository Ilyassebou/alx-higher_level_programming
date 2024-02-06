#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
