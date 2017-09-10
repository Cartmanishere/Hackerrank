
def reverse(x):
    return int(str(x)[::-1])

i, j, k = [int(i) for i in input().strip().split(' ')]
days = 0
for x in range(i, j+1):
    if abs(x-reverse(x))%k == 0:
        days += 1
        
print(days)
