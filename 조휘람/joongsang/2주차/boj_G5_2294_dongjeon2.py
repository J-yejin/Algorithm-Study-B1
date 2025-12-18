import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dongs = []
for _ in range(n):
    dongs.append(int(input()))

dp = [100000000] * (k + 1)

dp[0] = 0

for dong in dongs:
    for i in range(dong, k + 1):
        if dp[i - dong] !=100000000:
            dp[i] = min(dp[i], dp[i - dong] + 1)

if dp[k] == 100000000:
    print(-1)
else:
    print(dp[k])

