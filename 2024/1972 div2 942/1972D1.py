inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    s = input().split()
    n = int(s[0])
    m = int(s[1])
    ans = 0
    for i in range(1,m+1):
        ans += ((n//i + 1)//i)
    toPrint.append(ans-1)

for s in toPrint: print(s)