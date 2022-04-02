#!/usr/bin/env python3

import sys
from string import punctuation
import math

a = sys.stdin.readlines()
dict = {}

for s in a:
    s = s.strip().split(":")
    for char in s[1]:
        if char in punctuation:
            s[1] = s[1].replace(char, "")
    name = s[0]
    sale = s[1].split()
    sale = [int(nums) for nums in sale]
    average_sale = sum(sale) / len(sale)
    dict[name] = average_sale

sort = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for sale in sort:
    print(f"{sale[0]}: {sale[1]:.2f}")
