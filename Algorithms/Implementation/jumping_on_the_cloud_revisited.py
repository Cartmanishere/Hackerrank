#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
start = 0
end = None
E = 100
while end != 0:
    end = (start+k)%n
    start = end
    if c[end] == 0:
        E -= 1
    else:
        E -= 3
print(E)