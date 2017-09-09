#!/bin/python3

import sys

def sockMerchant(n, ar):
    visited = {}
    sock_pairs = 0
    for i in ar:
        try:
            visited[i] += 1
        except:
            visited[i] = 1
    
    for i in set(ar):
        sock_pairs += visited[i] // 2
    
    return sock_pairs

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
