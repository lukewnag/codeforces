def solve():
    n, m = map(int, input().split())
 
    ans = max((m+1)//2, (4*m+n+14)//15)
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()