from collections import deque

N = int(input())
L = deque(range(1,N+1))

while len(L) != 1:
    L.popleft()
    L.append(L.popleft())

print(L[0])
