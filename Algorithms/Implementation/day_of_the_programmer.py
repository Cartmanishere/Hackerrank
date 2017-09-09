#!/bin/python3

import sys

def solve(year):
    if year < 1918:
        if year % 4 == 0:
            return "%s.%s.%d" % ("12","09",year)
        else:
            return "%s.%s.%d" % ("13","09",year)
    elif year > 1918:
        if (year%400==0) or ( (year%4==0) and (year%100!=0)):
            return "%s.%s.%d" % ("12","09",year)
        else:
            return "%s.%s.%d" % ("13","09",year)
    else:
        return "%s.%s.%d" % ("26","09",year)
        
            


year = int(input().strip())
result = solve(year)
print(result)
