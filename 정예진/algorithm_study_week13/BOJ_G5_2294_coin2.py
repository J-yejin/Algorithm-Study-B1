# 접근방법 : dp..인데 이제 점화식이 1과는 조금 다른 양상이었음
# 1은 만들 수 있는 방법의 수를 세는거라면 2는 가능한 적은 개수의 동전으로 만드는 방법이 필요
# 이전 방법에 동전 한개를 더하는 것과 현재의 값 중 더 작은 것을 골라야 한다
# 배수에 갇혀서 한동안 방법을 못 떠올린 문제..

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [10001] * (k+1)
dp[0] = 0

for coin in coins:
    for val in range(coin, k+1):
        if coin > val:
            break
        dp[val] = min(dp[val-coin]+1, dp[val])

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])