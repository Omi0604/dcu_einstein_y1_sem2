#!/usr/bin/env python3

from math import ceil
import sys

def chocolate(n):
    n = int(n)
    nums_chocolate = n / 400
    print(ceil(nums_chocolate))


for lines in sys.stdin:
    chocolate(lines)
