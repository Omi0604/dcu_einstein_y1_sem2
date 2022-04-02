#!/usr/bin/env python3

import sys

def email(s):
    [left, _] = s.split("@")
    left = left.strip("0123456789")
    [first, second] = left.split(".")
    print(first.capitalize() + " " + second.capitalize())
    return


for s in sys.stdin:
    email(s)
