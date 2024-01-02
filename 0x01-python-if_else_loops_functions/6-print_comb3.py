#!/usr/bin/python3
for num in range(10):
    for next_num in range(num + 1, 10):
        print("{:d}{:d}".format(num, next_num),
                end=(", " if num < 8 or next_num < 9 else "\n"))
