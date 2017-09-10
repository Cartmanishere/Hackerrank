#!/bin/python3

import sys


h = list(map(int, input().strip().split(' ')))
word = input().strip()
heights = []
for i in word:
    heights.append(h[ord(i)-97])

print(len(word)*max(heights))