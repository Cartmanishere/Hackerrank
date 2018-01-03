#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    gc = 0
    for i in range(len(arr)):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc+=1
    return gc

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
