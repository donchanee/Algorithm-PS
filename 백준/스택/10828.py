#https://www.acmicpc.net/problem/10828 스택

import sys

N = int(sys.stdin.readline())
a = []
for i in range(N):
    b = sys.stdin.readline().rstrip()  # 파이썬의 input()은 느린방식이기 때문에 자꾸 시간초과가 발생했따.
    if b.split()[0] == 'push':
        a.append(b.split()[1])
    elif b == 'pop':
        try:
            print(a.pop())
        except:
            print(-1)
    elif b == 'size':
        print(len(a))
    elif b == 'empty':
        if not a:
            print(1)
        else:
            print(0)
    elif b == 'top':
        try:
            print(a[-1])
        except:
            print(-1)
