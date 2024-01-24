#!/usr/bin/python3

def magic_calculation(a, b):
    num = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception('Too far')
            num += (a ** b) / i
        except Exception:
            num += a + b
            break
    return num
