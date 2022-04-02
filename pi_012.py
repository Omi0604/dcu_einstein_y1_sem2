#!/usr/bin/env python3

import sys
from math import pi
for line in sys.stdin:
    print(f"{pi:.{int(line)}f}")
