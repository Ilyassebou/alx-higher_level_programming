#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list[1:]:
        max_value = num if num > max_value else max_value

    return max_value
