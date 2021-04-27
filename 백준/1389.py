import sys; input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
dic = [set() for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    dic[s].add(e)
    dic[e].add(s)

print(dic)

def BFS(start):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[1] = 1

    while q:
        tr = q.popleft()
        
        for i in dic[tr]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[tr] + 1
    cnt = 0
    for i in range(1, N+1):
        if visited[i] != 0:
            cnt += visited[i]

    return cnt - N

result = []
for i in range(1, N+1):
    result.append((i,BFS(i)))

print(sorted(result, key=lambda x:x[1]))

