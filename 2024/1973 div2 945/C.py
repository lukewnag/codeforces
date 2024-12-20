def solve():
    n = int(input())
    p = input().split()
    q = []
    for i in range(len(p)):
        p[i] = int(p[i])
        q.append(n+1-p[i])
    qEven = q[::2]
    qOdd = q[1::2]
    if 1 in qEven: # qEven should be bigger, we can make qOdds smaller
        for i in range(n//2):
            qOdd[i] -= 1
        unused = []
        used = set(qOdd)
        for i in range(1,n+1):
            if i not in used: unused.append(i)
        qEvenIdx = [(qEven[i], i) for i in range(n//2)]
        qEvenIdx.sort()
        for i in range(n//2):
            idx = qEvenIdx[i][1]
            qEven[idx] = unused[i]
    else:
        for i in range(n//2):
            qEven[i] -= 1
        unused = []
        used = set(qEven)
        for i in range(1,n+1):
            if i not in used: unused.append(i)
        qOddIdx = [(qOdd[i], i) for i in range(n//2)]
        qOddIdx.sort()
        for i in range(n//2):
            idx = qOddIdx[i][1]
            qOdd[idx] = unused[i]
    ans = []
    for i in range(n//2):
        ans.append(str(qEven[i]))
        ans.append(str(qOdd[i]))
    
    ans = ' '.join(ans)
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()

# n+1-p[i] everything so all a's are the same
# take all the even and odd indices separately, pick the one without n to have bigger sum?
# let's say even is bigger
# substitute each even for the next one bigger than the current
# same for odds, except use the next one smaller than current
# this might not work