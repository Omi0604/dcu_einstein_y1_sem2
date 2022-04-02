#!/usr/bin/env python3

import sys
Nums = list(range(0, 101))
numsE1 = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine", "ten"]
numsE2 = ["eleven", "twelve", "thirteen", "fourteen",
          "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numsE3 = ["twenty", "thirty", "forty", "fifty",
          "sixty", "seventy", "eighty", "ninety"]
lines = sys.stdin.readlines()


def main(line):
    i = 0
    while i < len(line):
        num = line[i]
        if int(num) in Nums:
            num = int(num)
            if 0 <= num and num <= 10:
                pos = num
                out = numsE1[pos]
                #print(out, numInt)
            elif 11 <= num and num <= 19:
                pos = num - 11
                out = numsE2[pos]
                #print(out, numInt)
            elif 20 <= num and num <= 99:
                d = num // 10 - 2
                u = num % 10
                if u == 0:
                    out = numsE3[d]
                else:
                    out = numsE3[d] + "-" + numsE1[u]
            elif num == 100:
                out = "one hundred"
            line[i] = out
        else:
            line[i] = num.replace(num, "unknown", 1)
        i += 1
    print(" ".join(line))


for line in lines:
    line = line.strip().split()
    main(line)
