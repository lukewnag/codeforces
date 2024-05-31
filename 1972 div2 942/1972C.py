inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    s = input().split()
    n, k = int(s[0]), int(s[1])
    a = input().split()
    for i in range(n): a[i] = int(a[i])
    a = sorted(a)

    if k >= n*a[-1] - (suma := sum(a)):
        freq = (k + sum(a))//n
        k = k + sum(a) - freq*n
        toPrint.append(n*(freq-1) + 1 + k)
    else:
        storage = {}
        for i in a:
            if i not in storage: storage[i] = 1
            else: storage[i] += 1 # occurrences of each freq
        # i = 0
        freqs = sorted(storage.keys()) # freqs
        minIdx = 0
        while minIdx+1 < len(freqs) and k >= (freqs[minIdx+1] - freqs[minIdx])*storage[freqs[minIdx]]:
            storage[freqs[minIdx + 1]] += storage[freqs[minIdx]]
            k -= (freqs[minIdx+1] - freqs[minIdx])*storage[freqs[minIdx]]
            minIdx += 1
        fr, cnt = freqs[minIdx], storage[freqs[minIdx]]
        finalMin = fr + k//cnt
        k = k % cnt
        numAtMin = cnt - k # rest get boosted up 1
        toPrint.append(n*(finalMin-1) + 1 + (n - numAtMin))
            
    # currMin = 0
    # for i in range(k):
    #     while currMin < n-1 and a[currMin] == a[currMin + 1]: currMin += 1
    #     a[currMin] += 1
    #     if currMin != 0: currMin -= 1
    # ans = n*a[0] - n + 1
    # for i in range(n):
    #     if a[i] > a[0]: ans += 1
    # toPrint.append(ans)

for s in toPrint: print(s)