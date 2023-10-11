#!/usr/bin/python3
def subtract_lesser_values(list_num):
    subtract = 0
    max_value = max(list_num)

    for num in list_num:
        if max_value > num:
            subtract += num

    return (max_value - subtract)


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    p = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numerals = list(p.keys())

    total = 0
    last_value = 0
    current_values = [0]

    for char in roman_string:
        for numeral in roman_numerals:
            if numeral == char:
                if p.get(char) <= last_value:
                    total += subtract_lesser_values(current_values)
                    current_values = [p.get(char)]
                else:
                    current_values.append(p.get(char))

                last_value = p.get(char)

    total += subtract_lesser_values(current_values)

    return (total)
