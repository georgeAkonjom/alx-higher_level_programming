#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    index = 0
    result = 0
    for letter in range(len(roman_string)):
        key = roman_string[letter]
        if len(roman_string) == 1:
            result += roman_num[roman_string[letter]]
            return result
        if index == 0:
            # print("val of first key: {}".format(roman_num[key]))
            if roman_num[roman_string[letter]] < roman_num[roman_string[letter + 1]]:
                result -= roman_num[key]
                print
                # print('first key is lesser than second')
                index += 1
                continue
        index += 1
        result += roman_num[key]
        # print(roman_num[key])
    # print('result: {}'.format(result))
    return(result)
