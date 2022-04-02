#!/usr/bin/env python3

import sys

vowels = "aeiou"

def plural(s):
    if (s[-1] == "s" or s[-1] == "z" or s[-1] == "x"):
        s = s + "es"
    elif (s[-2:] == "ch" or s[-2:] == "sh"):
        s = s + "es"
    elif s[-1] == "y" and (s[-2] not in vowels):
        s = s.replace(s[-1:], "ies", 1)
    elif s[-1] == "f":
        s = s.replace(s[-1:], "ves", 1)
    elif s[-2:] == "fe":
        s = s.replace(s[-2:], "ves", 1)
    elif s[-1] == "o":
        s = s + "es"
    else:
        s = s + "s"
    return s


for s in sys.stdin:
    t = plural(s.strip())
    print(t)
