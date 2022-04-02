#!/usr/bin/env python3

import sys

a = []
b = []
s = sys.stdin.readlines()

s[0] = s[0].strip().split()

for nums in s[0]:
    nums = int(nums)
    a.append(nums)

a.sort()

for letter in s[1]:
    if letter == "A":
        b.append(a[0])
    elif letter == "B":
        b.append(a[1])
    elif letter == "C":
        b.append(a[2])

print(b[0], b[1], b[2])
