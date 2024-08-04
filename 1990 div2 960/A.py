def solve():
    x = input()
    nums = list(map(int, input().split()))

    d = {s:0 for s in set(nums)}
    for n in nums: d[n] += 1
    
    newNums = [(a, b) for a, b in d.items()]
    
    for n in newNums:
        if n[1] % 2 == 1:
            print('yes')
            return

    print('no')

for _ in range(int(input())):
    solve()