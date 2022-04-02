#!/usr/bin/env python3

import sys

def sum_factors(n):
    total = 0
    for num in range(1, n):
        if n % num == 0:
            total = total + num
    return print(total == n)


for n in sys.stdin:
    sum_factors(int(n))
