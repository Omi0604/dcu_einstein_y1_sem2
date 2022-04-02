#!/usr/bin/env python3

import sys

def pangram(s):
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    a = [letter.lower() for letter in s if letter.lower() in all_letters]
    b = [letter for letter in all_letters if letter not in a]
    c = "".join(b)
    if len(b) == 0:
        print("pangram")
    else:
        print(f"missing {c}")


for lines in sys.stdin:
    pangram(lines)
