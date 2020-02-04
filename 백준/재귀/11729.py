# https://www.acmicpc.net/problem/11729 하노이의 탑

def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)

D = int(input())
M = 0

for i in range(D):
    M = M * 2
    M += 1

print(M)
hanoi(D, 1, 2, 3)
