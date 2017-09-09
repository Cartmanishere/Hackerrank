#!/bin/python3

import sys


q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if abs(abs(x)-abs(z)) > abs(abs(y)-abs(z)):
        print("Cat B")
    elif abs(abs(x)-abs(z)) == abs(abs(y)-abs(z)):
        print("Mouse C")
    else:
        print("Cat A")
