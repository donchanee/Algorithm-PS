import sys
N, M = map(int, input().split())
num = dict()
st = dict()

for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    num[str(i)] = name
    st[name] = i

for i in range(1, M+1):
    q = sys.stdin.readline().strip()
    if q in num:
        print(num[q])
    else:
        print(st[q])
