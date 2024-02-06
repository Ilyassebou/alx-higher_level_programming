#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file
    """
    t = ""
    with open(filename) as r:
        for line in r:
            t += line
            if search_string in line:
                t += new_string
    with open(filename, "w") as w:
        w.write(t)
