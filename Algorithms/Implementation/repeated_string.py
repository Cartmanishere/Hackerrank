#!/bin/python3

import sys

def get_num_a(st):
    count = 0
    for i in st:
        if i == "a":
            count += 1
            
    return count

s = input().strip()
n = int(input().strip())
length = len(s)
num_a = get_num_a(s)
print((num_a*(n//length))+get_num_a(s[:n%length]))


