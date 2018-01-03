#!/bin/python3

import sys


h = int(input().strip())
m = int(input().strip())

convertor = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three',
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine'
}

if m == 0:
    print(convertor.get(h)+" o' clock")
elif m==15:
    print("quarter past " + convertor.get(h))
elif m == 30:
    print("half past "+convertor.get(h))
elif m < 30:
    if m == 1:
        print("one minute past "+ convertor.get(h))
    else:
        print(convertor.get(m)+" minutes past " + convertor.get(h))

elif m == 45:
    print("quarter to " + convertor.get(h+1))
else:
    p = 60 - m
    if p == 1:
        print("one minute to "+ convertor.get(h+1))
    else:
        print(convertor.get(p)+" minutes to "+convertor.get(h+1))

    
    
