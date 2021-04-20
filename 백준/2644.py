from collections import deque, defaultdict
import sys
read = sys.stdin.readline

n = int(input())
visited = [0] * (n+1)
a, b = map(int, input().split())
dic = defaultdict(list)

m = int(input())
for _ in range(m):
    x, y = map(int, read().split())
    dic[x].append(y)
    dic[y].append(x)

q = deque()
q.append(a)
result = [0 for _ in range(n+1)]
visited[a] = 1

while q:
    t = q.popleft()
    
    for x in dic[t]:
        if not visited[x]:
            visited[x] = 1
            q.append(x)
            result[x] += result[t] + 1

print(result[b] if result[b] else -1)