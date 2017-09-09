#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    tot = 0
    for j in range(len(ar)):
        for i in range(j):
            if (ar[i]+ar[j])%k == 0:
                tot = tot + 1
                
    return tot
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
