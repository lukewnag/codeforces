inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    numProbs = int(input())
    actual = input().split()
    for i in range(numProbs): actual[i] = int(actual[i])
    exp = input().split()
    for i in range(numProbs): exp[i] = int(exp[i])
    
    actual.sort()

    added = 0
    while True:
        y = True
        for i in range(numProbs):
            if actual[i] > exp[i]:
                actual.insert(0, 1)
                added += 1
                y = False
                break
        if y:
            toPrint.append(added)
            break

for s in toPrint: print(s)