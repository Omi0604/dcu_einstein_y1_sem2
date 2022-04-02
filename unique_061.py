#!/usr/bin/env python3

import sys

def unique(n):
    n = n.strip().split()
    n = [int(nums) for nums in n]
    a = []
    for nums in n:
        count = n.count(nums)
        if count == 1:
            a.append(nums)
    if len(a) > 0:
        print(sorted(a)[-1])
    else:
        print("none")


for lines in sys.stdin:
    unique(lines)
