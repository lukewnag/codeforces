def solve():
    m, x = map(int, input().split())
    c, h = [], []
    for i in range(m):
        ci, hi = map(int, input().split())
        c.append(ci)
        h.append(hi)
    
    dp = {0: 0} # happiness level maps to balance
    for i in range(m):
        edge = {}
        for happy in dp: # happy = happiness level
            if dp[happy] - c[i] >= 0: # if enough money this month to buy more happiness
                edge[happy + h[i]] = dp[happy] - c[i]
        for e in edge:
            if e not in dp: dp[e] = edge[e]
            else: dp[e] = max(dp[e], edge[e])
        for happy in dp: dp[happy] += x
    
    k = dp.keys()
    ans = max(k)
    print(ans)

for _ in range(int(input())):
    solve()