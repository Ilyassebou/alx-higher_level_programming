#!/usr/bin/python3
for j in range(ord('z'), ord('a') - 1, -1):
    d = 0 if j % 2 == 0 else 32
    print('{}'.format(chr(j - d)), end='')
