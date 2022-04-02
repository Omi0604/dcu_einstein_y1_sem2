#!/usr/bin/env python3

import sys

for s in sys.stdin:
    upper = 0
    lower = 0
    digits = 0
    special = 0
    s = s.strip()
    for c in s:
        if c.isdigit():
            digits = 1
        elif c.isupper():
            upper = 1
        elif c.islower():
            lower = 1
        else:
            special = 1
    print(upper + lower + digits + special)
