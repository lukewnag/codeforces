def solve():
    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
 
    ans = [0 for i in range(n)]
    for i in range(y, x+1): ans[i] = 1
    binary = -1
    for i in range(x+1, n):
        ans[i] = binary
        binary *= -1
    binary = -1
    for i in range(y-1, -1, -1):
        ans[i] = binary
        binary *= -1

    ansStr = ' '.join([str(f) for f in ans])
    
    print(ansStr)

for _ in range(int(input())):
    solve()