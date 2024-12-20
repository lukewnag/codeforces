def solve():
    n = int(input())
    s = [*input()]

    r = set(s)
    sort = sorted(r)

    d = {}
    for i in range(len(sort)):
        d[sort[i]] = sort[len(sort) - 1 - i]
 
    t = [d[a] for a in s]
    ans = ''.join(t)
    
    print(ans)
 
# Example usage
for _ in range(int(input())):
    solve()