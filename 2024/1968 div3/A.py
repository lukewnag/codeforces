def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

def solve():
    x = int(input())
    ans = 0
    ans2 = 0
    for y in range(1,x):
        if y + gcd(x, y) > ans: 
            ans = y + gcd(x, y)
            ans2 = y
    
    print(y)
 

for _ in range(int(input())):
    solve()