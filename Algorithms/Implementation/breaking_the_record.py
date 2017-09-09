#!/bin/python3

import sys

def getRecord(s):
    max_x = 0
    min_x = 0
    for i in range(1, len(s)):
        if s[i] > max(s[0:i]):
            max_x = max_x + 1
        if s[i] < min(s[0:i]):
            min_x = min_x + 1
    return [max_x, min_x]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
