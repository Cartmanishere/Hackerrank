#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    
    
    if z>=abs(x-y):
        print(b*x+w*y)
    elif x <= y:
        print((b+w)*x+w*z)
    else:
        print((b+w)*y+b*z)
