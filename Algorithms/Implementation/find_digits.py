#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp = 0
    for i in str(n):
        if int(i) != 0:
            if n%int(i)==0:
                temp += 1
    print(temp)