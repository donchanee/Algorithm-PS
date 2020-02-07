'''
이 방법으로 해보고 싶음. 수정 필요

N, M = map(int, input().split())
cnt = [[0 for col in range(M)] for row in range(N)]
a = []
for i in range(N):
    a.append(input())
    
b = a[0][0]
min_to = 64

for i in range(M):
        for j in range(N):
            if a[i][j] == b and b == 'W':
                b = 'B'
            elif a[i][j] == b and b == 'B':
                b = 'W'
            else:
                cnt[i][j] = 1
                if b == 'W':
                    b = 'B'
                else:
                    b = 'W'
                    
for y in range(N-7):
    for x in range(M-7):
        pass
        

sum_to = 0
for i in cnt:
    sum_to += sum(i)

print(sum_to)
'''

N, M = map(int, input().split())
board = [input() for _ in range(N)]
w, b = 'WBWBWBWB', 'BWBWBWBW'
white = [w, b] * 4
black = [b, w] * 4

min_ = 64
for y in range(N-7):
    for x in range(M-7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[y+i][x+j] != white[i][j]:
                    cnt += 1
            if cnt > min_:
                break
        min_ = min(min_, cnt)
        cnt = 0
        for i in range(8):
            for j in range(8):
                if board[y+i][x+j] != black[i][j]:
                    cnt += 1
            if cnt > min_:
                break
        min_ = min(min_, cnt)

print(min_)

