#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for numeral in roman_string:
        if numeral not in roman_dict:
            return 0  # Invalid Roman numeral

        current_value = roman_dict[numeral]
        result += current_value

        if current_value > prev_value:
            result -= 2 * prev_value

        prev_value = current_value

    return result
