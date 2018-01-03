#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    choc = wrappers = n // c

    while (wrappers >= m):
        choc+= 1
        wrappers -= m - 1 
    print(choc)
        
        
