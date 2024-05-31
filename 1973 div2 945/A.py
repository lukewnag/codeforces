def solve():
    a, b, c = map(int, input().split())

    if (a+b+c)%2 == 1:
        print('-1')
        return
    if a+b >= c:
        print((a+b+c)//2)
        return
    
    print(a+b)
 
# Example usage
for _ in range(int(input())):
    solve()