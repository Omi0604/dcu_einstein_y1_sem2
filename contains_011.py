#!/usr/bin/env python3

import sys

def contains(chars, s):
    for c in chars:
        if c not in s:
            return False
        s = s.replace(c, '', 1)
    return True

def main():
    for line in sys.stdin:
        [chars, s] = line.strip().lower().split()
        print(contains(chars, s))


if __name__ == '__main__':
    main()
