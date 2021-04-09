import sys
from collections import defaultdict,deque

N, M = map(int, input().split())
visited = [0] * (N+1)
graph = defaultdict(list)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
result = 0
for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        q.append(i)
        result += 1

        while q:
            now = q.popleft()
            for j in graph[now]:
                if visited[j] == 0:
                    visited[j] = 1
                    q.append(j)

print(result)

# bfs
