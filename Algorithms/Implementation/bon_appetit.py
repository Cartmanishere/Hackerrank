#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    ar.pop(k)
    even_b = 0
    for i in ar:
        even_b = even_b + i/2
        
    if even_b == b:
        return "Bon Appetit"
    else:
        return int(b - even_b)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
