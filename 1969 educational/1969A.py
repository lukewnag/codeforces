inputs = []
numCases = int(input())
outputs = []
toPrint = []

for case in range(numCases):
    s = int(input())
    nums = input().split()
    for i in range(len(nums)): nums[i] = int(nums[i]) - 1
    numFixedPts = 0
    numPairs = 0
    for i in range(s):
        if nums[i] == i: numFixedPts += 1
        if numFixedPts >= 2: break
        if i == nums[nums[i]]:
            numPairs = 1
            # toPrint.append(2)
            break
    if numFixedPts >= 2: toPrint.append(1)
    elif numPairs == 1: toPrint.append(2)
    else: toPrint.append(3)

    # cyclens = []
    # # seen = set()
    
    # for i in range(s):
    #     seen = set()
    #     if i in seen: continue
    #     current = nums[i]
    #     cyclen = 0
    #     while current not in seen:
    #         seen.add(current)
    #         cyclen += 1
    #         current = nums[current]
    #     cyclens.append(cyclen)
    
    # toPrint.append(min(cyclens))

for s in toPrint: print(s)