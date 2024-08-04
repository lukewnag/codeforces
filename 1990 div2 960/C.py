def solve():
    n = int(input())
    a = list(map(int, input().split()))
 
    ans = sum(a)
    # keep track of important indices
    # if you have 2+ of an element, shift indices 1 to the right after each timestep; otherwise discard

    indices = []
    elements = []
    
    # first run thru
    seen = set()
    for i in range(n):
        if a[i] not in seen: seen.add(a[i])
        else:
            if (not indices) or a[i] > elements[-1]:
                indices.append(i)
                elements.append(a[i])
    
    # indices.append(n)
    # indicesUsed = [True for i in range(len(elements))]
    # canContinue = True
    # while canContinue:
    #     canContinue = False
    #     for i in range(len(elements)):
    #         if indicesUsed[i]:
    #             if indices[i+1] - indices[i] == 1 or indices[i] >= n: indicesUsed[i] = False
    #             else: canContinue = True
    #             ans += (indices[i+1] - indices[i])*elements[i]
    #             indices[i] += 1


    indices.append(n)
    keyIndices = []
    for i in range(len(elements)):
        if indices[i+1] - indices[i] > 1: keyIndices.append(i)
        ans += (indices[i+1] - indices[i])*elements[i]
        indices[i] += 1

    keyIndices.append(len(elements))
    for i in range(len(keyIndices)-1):
        idx1, idx2 = keyIndices[i], keyIndices[i+1]
        gap = indices[idx2] - indices[idx1]
        ans += ((n - indices[idx2])*gap + gap*(gap+1)//2) * elements[idx1]
    
    print(ans)

for _ in range(int(input())):
    solve()