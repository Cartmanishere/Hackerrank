n = int(input())
arr = [ int(i) for i in input().strip().split(" ") ]
count = 0
if sum(arr)%2!=0:
	print("NO")
else:
	for i in range(len(arr)):
		if arr[i]%2!=0:
			arr[i+1] += 1
			count += 2

	print(count)