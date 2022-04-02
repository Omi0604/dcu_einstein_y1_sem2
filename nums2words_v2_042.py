#!/usr.bin/env python3

import sys
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
lines = sys.stdin.readlines()

def num2words(s):
    i = 0
    while i < len(s):
        num = s[i]
        if num in nums:
            s[i] = num.replace(num, words[int(num)], 1)
        else:
            s[i] = num.replace(num, "unknown", 1)
        i += 1
    print(" ".join(s))


for line in lines:
    line = line.strip().split()
    num2words(line)
