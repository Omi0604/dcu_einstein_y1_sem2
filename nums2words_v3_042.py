#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    s = f.readlines()

dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

i = 0
for word in s:
    word = word.strip()
    english, other = word.split()
    if i in dict.keys():
        dict[i] = other
    i = i + 1

s = sys.stdin.readlines()


for input in s:
    a = []
    input = input.strip().split()
    for nums in input:
        if int(nums) in dict.keys():
            a.append(dict[int(nums)])
    print(" ".join(a))
