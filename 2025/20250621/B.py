# collisions between balls do not matter.
# just look at each individual ball, whether it eventually bounces in

def solve():
    n, s = map(int, input().split())
    ans = 0
 
    for i in range(n):
        dx, dy, x, y = map(int, input().split())
        if dx == dy:
            if x == y:
                ans += 1
        else:
            if x + y == s:
                ans += 1

    print(ans)

for _ in range(int(input())):
    solve()