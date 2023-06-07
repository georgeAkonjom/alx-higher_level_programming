#!/usr/bin/python3
def pow(a, b):
    if a is not None or b is not None:
        result = 1
        if a == 0:
            result = 0
            return result
        if b == 0:
            return result
        if b < 0:
            for i in range(abs(b)):
                result = result / a
            return result
        else:
            for i in range(abs(b)):
                result = result * a
    return result
