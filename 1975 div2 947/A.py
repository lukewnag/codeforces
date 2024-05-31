def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    numBreaks = 0
    for i in range(n-1):
        if a[i] > a[i+1]: numBreaks += 1
        if numBreaks > 1:
            print("No")
            return
    if a[-1] > a[0]: numBreaks += 1
    if numBreaks > 1: print('No')
    else: print("Yes")

for _ in range(int(input())):
    solve()