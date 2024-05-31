def solve():
    n, m = map(int, input().split())
    a = input()
    b = input()
    ans = 0
    pos = 0
    while pos < m:
        if ans == n: break
        if pos == m: break
        if a[ans] == b[pos]: ans += 1
        pos += 1
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()