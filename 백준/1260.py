import sys; input = sys.stdin.readline
from collections import deque
N, M, V = map(int, input().split())
dic = [[] for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    dic[s].append(e)
    dic[e].append(s)
    dic[s] = sorted(dic[s])
    dic[e] = sorted(dic[e])

def DFS(N, V):
    q = deque()
    q.append(V)
    visited = [0] * (N+1)
    result = []

    while q:
        tr = q.pop()
        
        if not visited[tr]:
            result.append(tr)
            visited[tr] = 1
            for i in dic[tr][::-1]:
                q.append(i)

    return result

def BFS(N, V):
    q = deque()
    q.append(V)
    visited = [0] * (N+1)
    result = []

    while q:
        tr = q.popleft()
        
        if not visited[tr]:
            result.append(tr)
            visited[tr] = 1
            for i in dic[tr]:
                q.append(i)

    return result

print(' '.join(map(str, DFS(N,V))))
print(' '.join(map(str, BFS(N,V))))