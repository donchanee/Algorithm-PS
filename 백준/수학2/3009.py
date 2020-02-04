# https://www.acmicpc.net/problem/3009 네 번째 점

a = []
b = []

for i in range(3):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

for i in range(3):
    if a.count(a[i]) == 1:
        c = a[i]
    if b.count(b[i]) == 1:
        d = b[i]

print(c, d)
