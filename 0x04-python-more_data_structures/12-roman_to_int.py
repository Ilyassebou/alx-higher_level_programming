#!/usr/bin/python3
def roman_to_int(roman_str):
    if not roman_str or type(roman_str) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_num = 0
    for i in range(len(roman_str)):
        if i > 0 and roman_dict[roman_str[i]] > roman_dict[roman_str[i - 1]]:
            roman_num += roman_dict[roman_str[i]] - 2 * roman_dict[roman_str[i - 1]]
        else:
            roman_num += roman_dict[roman_str[i]]
    return roman_num
