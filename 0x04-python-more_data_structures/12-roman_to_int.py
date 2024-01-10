#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}

    total_value = 0
    prev_numeral_value = 0

    for numeral in reversed(roman_string):
        current_numeral_value = roman_dict[numeral]

        if current_numeral_value >= prev_numeral_value:
            total_value += current_numeral_value
        else:
            total_value -= current_numeral_value

        prev_numeral_value = current_numeral_value

    return total_value

