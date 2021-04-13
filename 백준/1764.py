import sys
N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    a.add(sys.stdin.readline().strip())
for _ in range(M):
    b.add(sys.stdin.readline().strip())

print(len(a&b))
for i in sorted(list(a&b)):
    print(i)
