inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    useless = input()
    s = input()
    a = s.count('U')
    if a%2 == 1: toPrint.append('YES')
    else: toPrint.append("NO")

for s in toPrint: print(s)