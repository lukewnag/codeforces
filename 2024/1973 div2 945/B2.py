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

    bOr = a[:]
    for i in range(1,n):
        bOr = bOr[:-1]
        for j in range(n-i):
            bOr[j] |= a[i+j]
        if len(set(bOr)) == 1:
            print(i+1)
            return
    
    print(n)
 
# Example usage
for _ in range(int(input())):
    solve()

# recompute all