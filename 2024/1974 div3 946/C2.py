def solve():
    n = int(input())
    a = list(map(int, input().split()))
    aprime = set(a)
 
    ans = 0

    threes = [a[i:i+3] for i in range(n-2)]

    pos01, pos12, pos02 = {}, {}, {}
    threesCnt = {}
    for i in range(n-2):
        x = threes[i]
        if (x[0], x[1]) not in pos01: pos01[(x[0], x[1])] = 0
        if (x[1], x[2]) not in pos12: pos12[(x[1], x[2])] = 0
        if (x[0], x[2]) not in pos02: pos02[(x[0], x[2])] = 0
        pos01[(x[0], x[1])] += 1
        pos12[(x[1], x[2])] += 1
        pos02[(x[0], x[2])] += 1
        if (tup3 := (x[0], x[1], x[2])) not in threesCnt: threesCnt[tup3] = 0
        threesCnt[tup3] += 1
    
    for key in pos01: ans += (p := pos01[key])*(p-1)//2
    for key in pos12: ans += (p := pos12[key])*(p-1)//2
    for key in pos02: ans += (p := pos02[key])*(p-1)//2

    for key in threesCnt: ans -= 3*(p := threesCnt[key])*(p-1)//2
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()