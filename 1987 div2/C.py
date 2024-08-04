def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if n==1:
        print(a[0])
        return
    
    # after a[-1] timesteps, last flower is at 0
    aOld = a.copy()
    ans = a[-1]
    for i in range(n): # these are the end flowers
        a[n-1-i] = min(i, a[n-1-i])
        if i!=0 and a[n-1-i] > a[n-i]: a[n-1-i] = max(a[n-1-i]-a[i], a[n-i])

    # locMaxDiffs = [0 for i in range(n-1)]
    # for i in range(n-1):
    #     if a[i] > a[i+1]: locMaxDiffs[i] = a[i] - a[i+1]
    
    # if locMaxDiffs[-1] == 0: # last flower is at least as tall as 2nd-to-last
    #     h = a[-1] - a[-2] # progress it this many timesteps


for _ in range(int(input())):
    solve()