def solve():
    x = int(input())
    m = input()
    
    if x%2 == 1:
        print("NO")
        return
    n = m.count('N')
    s = m.count('S')
    e = m.count('E')
    w = m.count('W')

    if (n-s)%2 == 1 or (e-w)%2 == 1:
        print("NO")
        return
    
    finalx, finaly = (n-s)//2, (e-w)//2

    if finalx == 0 and finaly == 0:
        if x==2:
            print("NO")
            return
    
    r1n, r1s, r2e, r2w = 0,0,0,0
    # first finalx n/s goes to rover 1
    if finalx >= 0: r1n = finalx
    else: r1s = -finalx
    if finaly >= 0: r2e = finaly
    else: r2w = -finaly

    if r1n + r1s + r2e + r2w == 0:
        if n != 0:
            r1n = 1
            r1s = 1
        elif e != 0:
            r2e = 1
            r2w = 1

    ans = []
    for i in range(x):
        if m[i] == 'N':
            if r1n > 0:
                ans.append('R')
                r1n -= 1
            else: ans.append('H')
        if m[i] == 'S':
            if r1s > 0:
                ans.append('R')
                r1s -= 1
            else: ans.append('H')
        if m[i] == 'E':
            if r2e > 0:
                ans.append('R')
                r2e -= 1
            else: ans.append('H')
        if m[i] == 'W':
            if r2w > 0:
                ans.append('R')
                r2w -= 1
            else: ans.append('H')
 
    ans = ''.join(ans)
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()