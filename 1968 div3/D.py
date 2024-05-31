def play(p, a, start, n, k):
    newMaxes = [start] # strat: go until one of these newMaxes
    turn = 0
    pos = start
    seen = {pos}
    turns = {pos: 0}
    totPts = {pos: 0}
    while turn < k and p[pos] not in seen:
        turn += 1
        totPts[p[pos]] = totPts[pos] + a[pos]
        turns[p[pos]] = turn
        pos = p[pos]
        seen.add(pos)
        if a[pos] > a[newMaxes[-1]]:
            newMaxes.append(pos)
    maxPts = 0
    for mPos in newMaxes:
        t = turns[mPos]
        if t >= k: break
        pts = totPts[mPos]
        pts += a[mPos]*(k - t)
        if pts > maxPts: maxPts = pts
    return maxPts

def solve():
    n, k, pb, ps = map(int, input().split())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    for i in range(n): p[i] -= 1
    
    bodya = play(p, a, pb-1, n, k)
    sasha = play(p, a, ps-1, n, k)
    
    if bodya > sasha: print("Bodya")
    if bodya == sasha: print("Draw")
    if bodya < sasha: print("Sasha")
 
# Example usage
for _ in range(int(input())):
    solve()