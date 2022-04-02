#!/usr/bin/env python3

import sys

def repcomps(s):
    num = int(s) + 1
    num = list(range(1, num))
    i = 0
    while i < len(num):
        if not int(num[i]) % 3:
            num[i] = "X"
        i = i + 1
    print(f"Multiples of 3 replaced: {num}")


for line in sys.stdin:
    repcomps(line)
