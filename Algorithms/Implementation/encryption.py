#!/bin/python3

import sys
import math

s = input().strip()
x = int(math.ceil(math.sqrt(len(s))))
y = int(math.floor(math.sqrt(len(s))))
while y*x < len(s):
    y += 1
index = 0
enc = []
for i in range(y):
    temp = s[index:(x+index)]
    while len(temp) != x:
        temp += " "
    enc.append(temp)
    index = index + x

for k in range(x):    
    for j in list(map(lambda i:i[k], enc)):
        if j != " ":
            print(j, end="")
    print(" ", end="")