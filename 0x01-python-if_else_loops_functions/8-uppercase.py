#!/usr/bin/python3
def uppercase(str):
    for j in str:
        print("{:c}".format(ord(j) - 32) if 97 <= ord(j) <= 122 else j, end="")
    print()
