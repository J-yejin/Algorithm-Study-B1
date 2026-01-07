import sys
input = sys.stdin.readline

N = int(input())
num_lst = [*map(int, input().split())]
dp = [[0] * 21 for _ in range(N)]
res = num_lst.pop()
# print(dp)
dp[0][num_lst[0]] = 1
for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if j + num_lst[i] <= 20:
                dp[i][j + num_lst[i]] += dp[i - 1][j]
            if j - num_lst[i] >= 0:
                dp[i][j - num_lst[i]] += dp[i - 1][j]
print(dp[N - 2][res])