def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
 
    ans = 0
    if a[0] <= a[1]: ans = a[0]
    for i in range(1,n-1):
        if a[i] <= a[i+1] or a[i] <= a[i-1]:
            if a[i] > ans: ans = a[i]
        if a[i] < a[i+1] and a[i] < a[i-1]:
            if (sf := min(a[i+1], a[i-1])) > ans: ans = sf
    if a[-1] <= a[-2] and a[-1] > ans: ans = a[-1]
    
    print(ans)

for _ in range(int(input())):
    solve()