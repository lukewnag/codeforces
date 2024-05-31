def solve():
    m, x = map(int, input().split())
    c = list(map(int, input().split()))
    
    dp = [0] # happiness level maps to balance
    for i in range(m):
        currlen = len(dp)
        if dp[-1] >= c[i]: dp.append(0)
        for j in range(currlen-1, -1, -1):
            if dp[j] < c[i]: continue # cant afford
            dp[j+1] = max(dp[j+1], dp[j] - c[i])
        for i in range(len(dp)): dp[i] += x
    
    ans = len(dp) - 1
    print(ans)

for _ in range(int(input())):
    solve()