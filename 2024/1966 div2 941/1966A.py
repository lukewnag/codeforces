# from sys import stdin
inputs = []
# lines = input().split('\n')
numCases = int(input())
cnt = 0

for case in range(2*numCases):
    s = input().split()
    for i in range(len(s)): s[i] = int(s[i])
    if cnt%2 == 0:
        inputs.append(s)
    else:
        cards = {}
        for i in s:
            if i not in cards: cards[i] = 1
            else: cards[i] += 1
        freqs = []
        for card in cards.keys():
            freqs.append(cards[card])
        freqs.sort()
        inputs[-1].append(freqs)
    cnt += 1

for i in range(numCases):
    numCards = inputs[i][0]
    exchange = inputs[i][1]
    cardCount = inputs[i][2]

    if cardCount[-1] < exchange:
        print(numCards)
        continue
    
    print(exchange-1)
    # while (c:=max(cardCount)) >= exchange:
    #     idx = cardCount.index(c)
    #     exchanges = c - c%exchange
    #     cardCount[idx] = 

    # print(sum(cardCount))