n = int(input().strip())
elements = [ int(i) for i in input().split(' ') ]
visited = {}
for i in elements:
    try:
        visited[i] += 1
    except:
        visited[i] = 1

print(len(elements) - max(map(lambda i: visited[i], visited)))