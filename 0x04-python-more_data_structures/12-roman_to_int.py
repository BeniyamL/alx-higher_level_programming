#!/usr/bin/python3
def roman_to_int(roman_string):
    """function that converts roman to integer

    Arguments:
        roman_string: the given roman

    Returns:
        the correspoding integer value
    """
    Roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or type(roman_string) is not str:
        return 0
    num = 0
    i = 0
    while i < len(roman_string):
        num1 = Roman[roman_string[i]]
        if i + 1 < len(roman_string):
            if num1 >= Roman[roman_string[i + 1]]:
                num += num1
            else:
                num -= num1
        else:
            num += num1
        i = i + 1
    return num
