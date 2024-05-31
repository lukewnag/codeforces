def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return a*b//gcd(a, b)

def lcmSet(s: set):
    a = s.pop()
    while s:
        b = s.pop()
        a = lcm(a, b)
    return a

def solve():
    a = list(map(int, input().split()))
    elems = set(a)
    if len(elems) == 1:
        print('0')
        return
    
    totalLcm = lcmSet(a)
    if totalLcm not in elems:
        print(len(a))
        return
    elems.remove(totalLcm)

for _ in range(int(input())):
    solve()