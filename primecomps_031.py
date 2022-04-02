#!/usr/bin/env python3

import sys

for s in sys.stdin:
    num = [int(n) for n in range(2, (int(s) + 1))]
    prime = [n for n in num if all(n % v != 0 for v in range(2, (n // 2) + 1))]
    print(f"Primes: {prime}")
