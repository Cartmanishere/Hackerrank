## This program is correct but for some inputs it gives runtime error on hackerrank
## I couldn't figure out the mistake. Maybe you can..

def result(w):
    t = list(w[::-1])
    i = 0
    while t[i] <= t[i+1]:
        i += 1
        if i == len(t) -1:
            return "no answer"
    j = 0
    while t[j] < t[i+1]:
        j += 1
    t[i+1], t[j] = t[j], t[i+1]
    t[:i+1] = t[:i+1][::-1]
    return ''.join(t[::-1])

n = int(input())
for i in range(n):
    print(result(input()))
