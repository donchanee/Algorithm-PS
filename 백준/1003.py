T = int(input())

dp = [0, 0] * 41
dp[0] = [1, 0]
dp[1] = [0, 1]

N_List = []

for _ in range(T):
    N_List.append(int(input()))
    
maxNum = max(N_List)

for i in range(2, maxNum+1):
    dp[i] = [dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1]] # 바텀 업

for num in N_List:
    print(dp[num][0],dp[num][1])
