#!/bin/python3

import sys

def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)


n = int(input().strip())
print(factorial(n))