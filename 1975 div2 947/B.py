def solve():
    n = int(input())
    a = list(map(int, input().split()))

    x = min(a)
    rejects = []
    for i in range(n):
        if a[i]%x != 0: rejects.append(a[i])
    if not rejects:
        print("Yes")
        return
    y = min(rejects)
    for i in range(len(rejects)):
        if rejects[i]%y != 0:
            print('No')
            return
    print("Yes")

for _ in range(int(input())):
    solve()