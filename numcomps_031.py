#!/usr/bin/env python3

import sys

for line in sys.stdin:
    s = int(line.strip())
    a = []
    for i in range(1, s + 1):
        a.append(i)
    print(f"Multiples of 3: {[n for n in a if n % 3 == 0]}")
    print(f"Multiples of 3 squared: {[n * n for n in a if n % 3 == 0]}")
    print(f"Multiples of 4 doubled: {[n * 2 for n in a if n % 4 == 0]}")
    print(f"Multiples of 3 or 4: {[n for n in a if n % 3 == 0 or n % 4 == 0]}")
    print(f"Multiples of 3 and 4: {[n for n in a if n % 3 == 0 and n % 4 == 0]}")
