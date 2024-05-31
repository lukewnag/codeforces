def solve():
    n = int(input())
    a = list(map(int, input().split()))
    aprime = set(a)
 
    ans = 0

    threes = [a[i:i+3] for i in range(n-2)]

    pos01, pos12, pos02 = {}, {}, {}
    for i in range(n-2):
        x = threes[i]
        if (x[0], x[1]) not in pos01: pos01[(x[0], x[1])] = set()
        if (x[1], x[2]) not in pos12: pos12[(x[1], x[2])] = set()
        if (x[0], x[2]) not in pos02: pos02[(x[0], x[2])] = set()
        pos01[(x[0], x[1])].add(i)
        pos12[(x[1], x[2])].add(i)
        pos02[(x[0], x[2])].add(i)
    
    for key in pos01:
        s = pos01[key]
        for skey in s:
            x = threes[skey]
            ans += len(s) - 1
            ans -= len(s.intersection(pos12[(x[1], x[2])])) - 1
            # s.remove(skey)
    
    for key in pos12:
        s = pos12[key]
        for skey in s:
            x = threes[skey]
            ans += len(s) - 1
            ans -= len(s.intersection(pos01[(x[0], x[1])])) - 1
            # s.remove(skey)
    
    for key in pos02:
        s = pos02[key]
        for skey in s:
            x = threes[skey]
            ans += len(s) - 1
            ans -= len(s.intersection(pos12[(x[1], x[2])])) - 1
            # s.remove(skey)
    
    print(ans//2)
 
# Example usage
for _ in range(int(input())):
    solve()