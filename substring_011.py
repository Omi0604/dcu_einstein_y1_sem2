#!/usr/bin/env python3

import sys

def substring(s):
    return s[0].lower() in s[1].lower()


for line in sys.stdin:
    s = line.split()
    print(substring(s))
