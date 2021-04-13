import sys
import heapq

N = int(sys.stdin.readline())
h = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(h) > 0:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, x)
