#!/bin/python3

import sys

def minimumDistances(a):
    mini = sys.maxsize
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                if abs(i-j)<mini:
                    mini = abs(i-j)
    if mini == sys.maxsize:
        mini = -1
    return mini
        

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
