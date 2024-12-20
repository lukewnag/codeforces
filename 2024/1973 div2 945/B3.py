def solve():
    n = int(input())
    a = input().split()

    for i in range(n): a[i] = int(a[i])

    bOr = [a[0]]
    for i in range(1, n):
        bOr.append(a[i] | bOr[-1])
    final = bOr[-1]

    if len(set(a)) == 1:
        print('1')
        return

    bOr = [[] for i in range(n+1)]
    bOr[1] = a

    k = 1
    while 2*k < n:
        newBor = []
        for i in range(n+1-2*k):
            newBor.append(bOr[k][i] | bOr[k][i+k])
        if len(set(newBor)) == 1:
            break
        k *= 2
        bOr[k] = newBor
    # binary search
    lower, upper = k, min(n, 2*k)
    while (lower + upper)//2 not in [upper, lower]:
        newBor = []
        k = (upper+lower)//2
        for i in range(n+1-k):
            newBor.append(bOr[lower][i] | bOr[lower][i+k-lower])
        if len(set(newBor)) == 1: upper = k
        else: lower = k
        bOr[k] = newBor
    if len(set(newBor)) == 1: print(k)
    else: print(k+1)
    
 
# Example usage
for _ in range(int(input())):
    solve()

# modified binary search
# size 16: 1, 2, 4, 8, 12, 14, 15
# when doing or for next doubling step:
# ex. 4 --> 8 do i[3] | i[7]