def purge(pts):
    l = []
    maxBalance = 0
    start = 0
    for i in range(len(pts)):
        if pts[i][0] != 0: # nonzero happiness; zero happiness used as baseline
            slope = pts[i][1]/pts[i][0]
            l.append(-slope, pts[i][0], pts[i][1])
        if pts[i][1] > maxBalance:
            maxBalance = pts[i][1]
            start = pts[i]
    l.sort() # ordered in decreasing slope
    purged = [start]
    for i in range(len(pts)-1):
        if pts[i][1] <= pts[i+1][1] and pts[i][2] <= pts[i+1][2]: pass
        # do a convex hull thing to purge idk how tho

def solve():
    m, x = map(int, input().split())

    # (happiness, balance)
    dp = [(0,0)]
    for i in range(m):
        c, h = map(int, input().split())
        prev = dp
        dpi = []
        for line in prev:
            balance, happiness = line[1], line[0]
            if c!= 0: dpi.append((happiness, balance+x))
            if balance>=c: dpi.append((happiness+h, balance+x-c))
        dp = dpi

 
    ans = max(dp)[0]
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()