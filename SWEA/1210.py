for _ in range(10):
    case = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for j in range(100): # 열
        x = j # 시작점
        i = 0
        if ladder[i][j]:
            while i < 99: # 행
                if j != 0 and ladder[i][j-1] and stat != 'r':
                    j -= 1
                    stat = 'l'
                elif j != 99 and ladder[i][j+1] and stat != 'l':
                    j += 1
                    stat = 'r'
                else:
                    i += 1
                    stat = 'b'


        if ladder[i][j] == 2:
            print("#",case," ",x,sep="")
            break

'''
for _ in range(10):
    case = int(input())
    max = 0
    a = [list(map(int, input().split())) for _ in range(100)]

    x = a[99].index(2)
    y = 99

    for _ in range(100):
        if a[y][x-1] == 1 and x != 0:
            a[y][x-1] = 0
            x -= 1
        elif a[y][x+1] == 1 and x != 99:
            a[y][x+1] = 0
            x += 1
        else:
            y -= 1

    print("#",case," ",x,sep="")
    
    수정 필요.
'''
