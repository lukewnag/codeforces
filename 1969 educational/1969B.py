inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    s = input()
    oneSeen = False
    zeroLocs = []
    oneLocs = []
    first1 = 0
    for i in range(len(s)):
        if not oneSeen and s[i] == '1':
            oneSeen = True
            first1 = i
        if oneSeen:
            if s[i] == '0': zeroLocs.append(i - first1)
            if s[i] == '1': oneLocs.append(i - first1)
    if not oneSeen: 
        toPrint.append(0)
        continue
    onePointer = 0 # location of last 1 before the current 0
    score = 0
    swaps = 0
    for i in range(len(zeroLocs)):
        while onePointer < len(oneLocs) - 1 and oneLocs[onePointer + 1] < zeroLocs[i]:
            onePointer += 1
        if onePointer >= len(oneLocs): break
        lengthToSwap = onePointer + 2 - swaps
        score += lengthToSwap
    toPrint.append(score)

for s in toPrint:
    print(s)