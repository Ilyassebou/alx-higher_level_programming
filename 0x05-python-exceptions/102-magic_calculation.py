#!/usr/bin/python3

def magic_calculation(a, b):
    num = 0
    for i in range(1, 4):
        if i > a:
            try:
                raise Exception('Too far')
            except Exception:
                num += a + b
                break
        else:
            num += (a ** b) / i
    return num
