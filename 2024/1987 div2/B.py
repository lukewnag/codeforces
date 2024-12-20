def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # localMaxIdx = [0]
    # for i in range(1,n):
    #     if a[i] > a[localMaxIdx[-1]]: localMaxIdx.append(i)
    
    improvements = [0]
    currLocMax = 0
    for i in range(1,n):
        if a[i] > a[currLocMax]: currLocMax = i
        if a[i] < a[currLocMax]: improvements.append(a[currLocMax] - a[i])
    improvements.sort()

    ans = 0
    for i in range(1,len(improvements)):
        ans += (1 + len(improvements) - i) * (improvements[i] - improvements[i-1])
    
    print(ans)

for _ in range(int(input())):
    solve()