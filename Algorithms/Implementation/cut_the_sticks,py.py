#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
temp = arr
start = []
while 0 not in start:
    min_ = min(temp)
    print(len(temp))
    start = [ i - min_ for i in temp if i - min_ != 0]
    temp = start
