def solve():
    n, m = map(int, input().split())
 
    ans = 1 + (n-1)*m
    
    print(ans)

for _ in range(int(input())):
    solve()