from sys import stdin

N = int(input())
A = []

for i in range(N):
    arr = stdin.readline().split()
    com = arr[0]
    
    if com == 'push':
        A.append(arr[1])
    elif com == 'pop':
        print(A.pop(0) if len(A) else -1)
    elif com =='size':
        print(len(A))
    elif com == 'empty':
        print(0 if len(A) else 1)
    elif com == 'front':
        print(A[0] if len(A) else -1)
    elif com == 'back':
        print(A[-1] if len(A) else -1)
