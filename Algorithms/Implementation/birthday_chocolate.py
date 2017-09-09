#!/bin/python3

import sys

def get_sum(some):
    tot = 0
    for i in some:
        tot = tot + i
    
    return tot

def solve(n, s, d, m):
    combinations = []
    for i in range(n-m+1):
        combinations.append(s[i:i+m])
    
    tot = 0
    for i in combinations:
        if get_sum(i) == d:
            tot = tot + 1
    
    return tot

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
