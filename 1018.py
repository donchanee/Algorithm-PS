# 8*8로 잘라야함

N, M = map(int, input().split())
a = []
cnt = 0
for i in range(N):
    a.append(input())

if a[0][0] == 'W':
    flag = 'W'
else:
    flag = 'B'

for i in a:
    for j in range(0, M):
        if i[j] == flag and flag == 'W':
            flag = 'B'
        elif i[j] == flag and flag == 'B':
            flag = 'W'
        else:
            cnt += 1
            
print(cnt-N)
