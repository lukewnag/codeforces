inputs = []
numCases = int(input())
outputs = []

for case in range(numCases):
    s = input().split()
    height, width = int(s[0]), int(s[1])
    if height == 1:
        board = input()
        if board[0] == board[-1]: outputs.append("YES")
        else: outputs.append("NO")
        continue
    if width == 1:
        start, end = 0,0
        for i in range(height):
            char = input()
            if i == 0: start = char
            if i == height-1: end = char
        if start == end: outputs.append("YES")
        else: outputs.append("NO")
        continue

    bottomleft, bottomright, topleft, topright = 0,0,0,0
    toprow, bottomrow = 0,0
    leftcol, rightcol = [], []
    for row in range(height):
        chars = input()
        if row == 0:
            topleft = chars[0]
            topright = chars[-1]
            toprow = chars
        if row == height-1:
            bottomleft = chars[0]
            bottomright = chars[-1]
            bottomrow = chars
        leftcol.append(chars[0])
        rightcol.append(chars[-1])
        
    if not ((bottomleft == bottomright and topleft == topright and bottomleft != topright) or
             (bottomleft == topleft and bottomright == topright and bottomleft != topright)): outputs.append('YES')
    else:
        if bottomleft == bottomright:
            bottomCh = bottomleft
            topCh = topright
            if topCh in bottomrow or bottomCh in toprow: outputs.append('YES')
            else: outputs.append('NO')
            continue
        if bottomleft == topleft:
            leftCh = bottomleft
            rightCh = topright
            if leftCh in rightcol or rightCh in leftcol: outputs.append('YES')
            else: outputs.append('NO')
            continue

for s in outputs: print(s)