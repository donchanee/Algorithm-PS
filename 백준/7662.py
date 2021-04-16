import sys
import heapq

TC = int(input())

for _ in range(TC):
    max_heap = []
    min_heap = []   
    k = int(input())

    for _ in range(k):
        string, n = sys.stdin.readline().strip().split()

        if string == 'I':
            heapq.heappush(min_heap, int(n))
            heapq.heappush(max_heap, (-int(n), int(n)))
        else:
            if n == '1' and len(max_heap) > 0:
                m = heapq.heappop(max_heap)
            elif n == '-1' and len(min_heap) > 0:
                m = heapq.heappop(min_heap)
    
    result = set([x[1] for x in max_heap]) & set(min_heap)

    if len(result) > 1:
        print(max(result), min(result))
    else:
        print('EMPTY')