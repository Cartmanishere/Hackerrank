#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n == 0:
        print(1)
    else:
        h = 1
        for i in range(n):
            if i%2==0:
                h = h*2 
            else:
                h += 1
        print(h)