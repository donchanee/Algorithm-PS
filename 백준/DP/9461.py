T= int(input())
L = [0] * 101
L[0] = 1
L[1] = 1
L[2] = 1

for i in range(3,101):
    L[i] = L[i-3] + L[i-2]

for i in range(T):
    N = int(input())
    print(L[N-1])
    
