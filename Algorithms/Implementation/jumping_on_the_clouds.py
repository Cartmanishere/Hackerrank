#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
current = 0
count = 0
while current != (n-1):
    try:
        if c[current+2] == 0:
            current += 2
        else:
            current += 1
    except:
        current += 1
    count += 1
    
print(count)