def solve():
    n = int(input())
    a = input().split()

    for i in range(n): a[i] = int(a[i])

    bOr = [a[0]]
    for i in range(1, n):
        bOr.append(a[i] | bOr[-1])
    
    final = bOr[-1]
    for i in range(n-1, -1, -1):
        if bOr[i] != final:
            print(i+2)
            return
    
    print(1)
 
# Example usage
for _ in range(int(input())):
    solve()

# take bitwise or of everything
# iterate down on k, taking bitwise or of 0-k
# when this is no longer stable you stop


# Binary search on bitwise or of whole set
# log N * n^2