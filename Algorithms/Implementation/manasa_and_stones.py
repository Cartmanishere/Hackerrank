for _ in range(int(input())):
	n, a, b = int(input()), int(input()), int(input())
	if a==b:
		print(a*(n-1))
	else:
		res = set()
		for i in range(n):
			res.add(a*(n-i-1) + b*i)

		for i in sorted(res):
			print(str(i)+" ", end="")
		print()
