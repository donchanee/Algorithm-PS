from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)
time = [0] * 100001

while q:
    v = q.popleft()
    if v == K:
        print(time[v])
        break
    for s in [v-1, v+1, v*2]:
        if 0<=s<100001 and not time[s]:
            time[s] = time[v] + 1
            q.append(s)
