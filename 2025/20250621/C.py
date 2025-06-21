def solve():
    n, m = map(int, input().split())

    biggest_number = n
    s = n*(n+1)//2

    if m < n or m > s:
        print(-1)
        return

    while s > m:
        biggest_number -= 1
        s -= biggest_number
    
    l = list(range(biggest_number, 0, -1))

    diff = m - s
    if diff == 0:
        l += list(range(biggest_number+1, n+1))
    else:
        idx = 0
        l.append(0)
        for i in range(diff+1):
            idx = len(l)-1 - i
            l[idx] += 1

        l[idx] = biggest_number+1
        l += list(range(biggest_number+2, n+1))

    print(l[0])
    for i in range(n-1):
        to_print = str(l[i]) + ' ' + str(l[i+1])
        print(to_print)
 
    # ans = 0
    
    # print(ans)

for _ in range(int(input())):
    solve()