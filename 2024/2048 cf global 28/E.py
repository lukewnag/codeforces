def solve():
    n, m = map(int, input().split())
 
    if n <= m//2:
        print('NO')
        return
    print('YES')
    
    if n >= m:
        toPrint = ' '.join([str(i+1) for i in range(m)])
        for i in range(2*n):
            print(toPrint)
        return
    
    # n < m < 2n
    # go L1 to R1 to L2 to R2 to ... until no more R's to traverse
    # then go L2 to R0 (Rm) to L3 to R1 to ... 

for _ in range(int(input())):
    solve()