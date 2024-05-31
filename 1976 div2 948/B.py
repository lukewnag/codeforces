def solve():
    n = int(input())

    l = []
    while n != 0:
        l.append(n%2)
        n = n//2
 
    l.append(0)
    l.append(0)

    for i in range(len(l)-1):
        if l[i] == 1 and l[i+1] == 1:
            stopidx = i+2
            while stopidx < len(l) and l[stopidx] == 1: stopidx += 1
            l[i] = -1
            for j in range(i+1, stopidx): l[j] = 0
            l[stopidx] = 1
        if l[i] == -1 and l[i+1] == 1:
            l[i] = 1
            l[i+1] = 0
    
    print(len(l))
    l = map(str, l)
    print(' '.join(l))

for _ in range(int(input())):
    solve()