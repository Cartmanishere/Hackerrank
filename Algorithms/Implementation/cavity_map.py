mapp = []
n = int(input())
for _ in range(n):
	a = [ int(i) for i in input().strip() ]
	mapp.append(a)

cavities = []
for i in range(1,n-1):
	for j in range(1,n-1):
		c = mapp[i][j]
		if c > mapp[i-1][j] and c > mapp[i+1][j] and c > mapp[i][j-1] and c > mapp[i][j+1]:
			cavities.append((i,j))


for i in range(n):
	for j in range(n):
		if (i,j) in cavities:
			print('X', end="")
		else:
			print(mapp[i][j], end="")
	print()