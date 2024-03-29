#!/usr/bin/python3
"""Log parsing script."""
import sys

total_size = 0
codes = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
iteration = 0


def print_stats():
    """Function that prints a resume of the stats."""
    print("File size: {}".format(total_size))
    for k, v in sorted(codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        line = line.split()
        if len(line) >= 2:
            if line[-2] in codes:
                codes[line[-2]] += 1
            try:
                total_size += int(line[-1])
            except ValueError:
                pass

        iteration += 1
        if iteration % 10 == 0:
            print_stats()

    print_stats()

except KeyboardInterrupt:
    print_stats()
