def solve():
    aLen = int(input())
    x = list(map(int, input().split()))
    
    ans = [x[0] + 1]
    for i in range(aLen-2):
        a = x[i]
        a += a*((x[i+1]-a)//a)
        ans.append(a)
    ans.append(x[-1])

    for i in range(aLen): ans[i] = str(ans[i])
    toPrint = ' '.join(ans)
    print(toPrint)
 
# Example usage
for _ in range(int(input())):
    solve()