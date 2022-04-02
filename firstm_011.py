#!/usr/bin/env python3

import sys

def first_m(s):
    return(s.replace("m", "M", 1))


for lines in sys.stdin:
    print(first_m(lines).strip())
