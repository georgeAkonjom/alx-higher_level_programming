#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10,
           'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    index = 0
    result = 0

    if not roman_string:
        return None
    for letter in range(len(roman_string)):
        key = roman_string[letter]
        if len(roman_string) == 1:
            result += num[roman_string[letter]]
            return result
        if index == 0:
            # print("val of first key: {}".format(num[key]))
            if num[roman_string[letter]] < num[roman_string[letter + 1]]:
                result -= num[key]
                print
                # print('first key is lesser than second')
                index += 1
                continue
        index += 1
        result += num[key]
        # print(num[key])
    # print('result: {}'.format(result))
    return(result)
