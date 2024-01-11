#!/usr/bin/python3
def roman_to_int(roman_string):
    numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_value = 0
    previous_value = 0

    if type(roman_string) is str and roman_string:
        for index in range(len(roman_string) - 1, -1, -1):
            if numeral_values[roman_string[index]] >= previous_value:
                total_value += numeral_values[roman_string[index]]
            else:
                total_value -= numeral_values[roman_string[index]]
            previous_value = numeral_values[roman_string[index]]
    return total_value
