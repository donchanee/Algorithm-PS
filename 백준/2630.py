from collections import defaultdict, deque

N = int(input())
c = int(input())
dic = defaultdict(list)
visited = [0] * (N+1)

for i in range(c):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

q = deque()
q.append(1)

while q:
    t = q.popleft()
    for i in dic[t]:
        if not visited[i]:
            q.append(i)
            visited[i] = 1

print(sum(visited) - 1)
