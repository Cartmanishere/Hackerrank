def isKaprekar(num):
	p = str(num**2)
	if len(p)%2 != 0:
		p = '0'+p
	n = int(p[:len(str(num))])
	if p[len(str(num)):] != '':
		m = int(p[len(str(num)):])
	else:
		m = 0
	if (n+m) == num:
		return True
	else:
		return False


p, q = int(input()), int(input())
count = 0
res = []
for i in range(p, q+1):
	if isKaprekar(i):
		count += 1
		res.append(i)

if count == 0:
	print("INVALID RANGE")
else:
	for i in res:
		print("{} ".format(i), end="")
