import sys

N = int(input())
s = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    s.append([a,b])
s = sorted(s, key=lambda a : a[0])
s = sorted(s, key=lambda a : a[1])

last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)