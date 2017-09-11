# Enter your code here. Read input from STDIN. Print output to STDOUT
input('')
p = [int(i) for i in input().strip().split(' ')]

for i in range(1, len(p)+1):
    print(p.index(p.index(i)+1)+1)