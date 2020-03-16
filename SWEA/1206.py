for j in range(10):
    T = int(input())
    cnt = 0
    a = list(map(int, input().split()))
    for i in range(2, T-2):
        b = max(a[i-2], a[i-1], a[i+1], a[i+2])
        if b < a[i]:
            cnt += a[i]-b
            
    print("#",j+1," ",cnt,sep="")

// 주변 4개 건물을 높이 중 최댓값을 구하고 현재 건물 높이보다 작다면 뺀 값을 cnt에 합하여 출력
