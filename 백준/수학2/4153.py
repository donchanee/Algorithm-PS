# https://www.acmicpc.net/problem/4153 직각삼각형

while True:
    x,y,z = map(int, input().split())
    if x==0 and y==0 and z==0:
        break
    if x*x+y*y == z*z:
        print('right')
    else:
        print('wrong')
