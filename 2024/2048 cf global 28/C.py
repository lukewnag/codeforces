def solve():
    # pick full string
    # pick other substring to have its first bit be at the location where first one first hits 0
    # if full string first hits 0 at index x out of total length y, then other substring must have length y-x
    s = input()
    firstZero = 0
    for i in range(len(s)):
        if s[i] == '0':
            firstZero = i
            break
    if firstZero == 0:
        print(f'{1} {len(s)} {1} {1}')
        return
    ans = 0
    l = len(s) - firstZero
    bestAns = [0 for i in range(l)] # xor, start from index firstZero
    sInt = int(s, 2)
    for start in range(firstZero):
        if s[start] == '0':
            continue
        x = []
        better = False
        for i in range(l):
            if s[start+i] == s[firstZero+i]: # in this case xor is 0 at this idx
                if not better and bestAns[i] == 1:
                    break
                x.append(0)
            else:
                x.append(1)
                if bestAns[i] == 0:
                    better = True
        if better:
            bestAns = x
            ans = start
            

    print(f'1 {len(s)} {ans+1} {ans + l}')

for _ in range(int(input())):
    solve()