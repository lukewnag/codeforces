def solve():
    n, k = map(int, input().split())
 
    # n numbers, length k
    big_nums = list(range(1 + n//k, n+1))
    small_nums = list(range(1, 1 + n//k))

    ans = []
    big_count = 0
    small_count = 0
    for i in range(n):
        if i%k == k-1:
            ans.append(str(small_nums[small_count]))
            small_count += 1
        else:
            ans.append(str(big_nums[big_count]))
            big_count += 1
    
    print(' '.join(ans))

for _ in range(int(input())):
    solve()