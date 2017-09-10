n = int(input().strip())
init = 5
liked = 0
for i in range(n):
    liked += init // 2
    init = (init // 2)*3
print(liked)