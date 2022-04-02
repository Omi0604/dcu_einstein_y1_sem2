#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
big = 0
for c in lines:
    c = c.rstrip("\n")
    if len(c) > big:
        big = len(c)

for c in lines:
    s = c.rstrip("\n")
    print(f"{s: ^{big}}")
