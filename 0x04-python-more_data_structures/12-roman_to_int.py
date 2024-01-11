#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    numeral_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [numeral_values[x] for x in roman_string] + [0]
    total_value = 0

    for index in range(len(numbers) - 1):
        if numbers[index] >= numbers[index + 1]:
            total_value += numbers[index]
        else:
            total_value -= numbers[index]

    return total_value
