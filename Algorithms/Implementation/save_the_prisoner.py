#!/usr/bin/env python3

T = int(input().strip())
for _ in range(T):
    N,M,S = list(map(int, input().strip().split()))
    print(((S - 1 + M - 1) % N) + 1)