#!/usr/bin/env python3

import sys

def upper(s):
    letters_upper = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
    upper = [letter for letter in s if letter in letters_upper]
    a = "".join(upper)
    print(a)


for lines in sys.stdin:
    upper(lines)
