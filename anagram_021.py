#!/usr/bin/env python3

import sys

def anagram(s):
    (left, right) = s.strip().split()
    if sorted(left) == sorted(right):
        print("True")
    else:
        print("False")


for s in sys.stdin:
    anagram(s)
