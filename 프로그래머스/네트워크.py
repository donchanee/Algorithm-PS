from collections import deque

def BFS(x, computers, visited):
    q = deque()
    q.append(x)
    
    while q:
        x = q.popleft()
        visited[x] = 1
        
        for idx, i in enumerate(computers[x]):
            if i and not visited[idx]:
                q.append(idx)
    
    return visited

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for x in range(n):
        if not visited[x]:
            answer += 1
            visited = BFS(x, computers, visited)
    
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))