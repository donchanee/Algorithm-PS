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
        

'''
위 코드는 오답
아래 코드는 정답
'''

import sys;read=sys.stdin.readline
import heapq

result=[]
for T in range(int(read())):
    visited=[False]*1_000_001
    minH,maxH=[],[]
    for i in range(int(read())):
        s=read().split()
        if s[0]=='I':
            heapq.heappush(minH,(int(s[1]),i))
            heapq.heappush(maxH,(-int(s[1]),i))
            visited[i]=True
        elif s[1]=='1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]]=False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]]=False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
    result.append(f'{-maxH[0][0]} {minH[0][0]}'if maxH and minH else'EMPTY')
print('\n'.join(result))
