# DOES NOT WORK

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    ans = 0
    idxToRemove = -1
    for i in range(n-2, -1, -1):
        if a[i] == i+1:
            idxToRemove = i
            break
    while idxToRemove >= 0:
        a = a[:idxToRemove] + a[idxToRemove+2:]
        ans += 1
        idxToRemove = -1
        for i in range(len(a)-2, -1, -1):
            if a[i] == i+1:
                idxToRemove = i
                break
    
    print(ans)

for _ in range(int(input())):
    solve()