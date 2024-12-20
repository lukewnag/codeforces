def solve():
    n, m = map(int, input().split())
 
    if n<m: print('No')
    elif (n-m)%2 == 0: print("Yes")
    else: print("No")

for _ in range(int(input())):
    solve()