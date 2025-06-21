def solve():
    dims = list(map(int, input().split()))
    x = [dims[i] for i in range(0, 6, 2)]
    y = [dims[i] for i in range(1, 6, 2)]
    sum = 0
    for i in range(3):
        sum += x[i] * y[i]
    length = int(sum**0.5)
    if length ** 2 != sum or max(dims) != length:
        print('NO')
        return
    if y[0] == length:  # x is going to be the aligning axis
        z = y.copy()
        y = x
        x = z
    if x[1] == x[2] and x[1] == length and y[0] + y[1] + y[2] == length:
        print('YES')
        return
    if y[1] == y[2] and y[1] + y[0] == length and x[1] + x[2] == length:
        print('YES')
        return
    print('NO')

for _ in range(int(input())):
    solve()