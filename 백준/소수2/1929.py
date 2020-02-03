# https://www.acmicpc.net/problem/1929 소수구하기

num_M, num_N = map(int, input().split(' '))

def is_prime(num):
    if(num<=1):
        return False
    
    i=2
    while i*i <= num:
        if num%i ==0:
            return False
        i += 1

    return True

for i in range(num_M, num_N+1):
    if(is_prime(i)):
        print(i)
