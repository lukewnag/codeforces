# DOES NOT WORK

inputs = []
numCases = int(input())
outputs = []
toPrint = []
from math import gcd

for case in range(numCases):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    ans = 0
    for div in range(1,min(m, n)):
        maxPoss = min(m, n)
        for i in range(div, maxPoss+1, div): # this is x+y
            for y in range(1, i):
                if gcd(i, y) != 1: continue
                x = i - y
                if div*x <= n and div*y <= m: ans += 1

    toPrint.append(ans)

for s in toPrint: print(s)