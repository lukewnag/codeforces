def solve():
    # Don't care about problems and contestants with rating <= kevin's

    # 1 <= n, m <= 3 * 10**5
    n, m = map(int, input().split()) #num participants, num problems
    ppl = list(map(int, input().split())) # participants
    prob = list(map(int, input().split())) # problems
    kevin = ppl[0]

    # iterate over all k from 1 to m, obtain min ranking for kevin
    # want to maximize the number of times kevin ties with someone better than him
    # so we should try to maximize the number of problems thrown out
    # to pick problems to throw out, start from kevin's rating and throw out problems above that

    # throw out all participants worse than or equal to kevin to make it easier
    newppl = []
    for p in ppl:
        if p > kevin:
            newppl.append(p)
    newppl.sort()
    prob.sort()
    if kevin >= prob[-1]:
        #kevin wins all
        print(' '.join([str(m//k) for k in range(1, m+1)]))
        return

    kevinProb = 0 # easiest problem kevin cannot do
    while kevin >= prob[kevinProb]:
        kevinProb += 1

# O(n log n) up to here
# Loop below was originally O(n^2); now O(m log m)
    easiestToTiesMap = {} # maps easiest problem to how many kevin ties there are
    ans = []
    for k in range(1, m+1): # number of problems in each contest
        numProbsThrown = m%k # start at kevinProb, go til kevinProb + numProbsThrown
        score = 0
        numKevinTies = 0
        for c in range(m//k): # old: O(n) loop (numKevinTies); now O(m/k)
            if kevinProb + numProbsThrown + c*k < len(prob):
                easiestProblem = prob[kevinProb + numProbsThrown + c*k]
                if easiestProblem in easiestToTiesMap:
                    numKevinTies = easiestToTiesMap[easiestProblem]
                else:
                    while numKevinTies < len(newppl) and newppl[numKevinTies] < easiestProblem:
                        numKevinTies += 1
                    easiestToTiesMap[easiestProblem] = numKevinTies
                score += 1 + len(newppl) - numKevinTies
            else:
                score += 1
        ans.append(str(score))
    
    print(' '.join(ans))

for _ in range(int(input())):
    solve()