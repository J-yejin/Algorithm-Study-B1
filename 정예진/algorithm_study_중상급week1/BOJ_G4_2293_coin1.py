# 접근 방법 : 머리 터질 거 같은 DP,, 근데 이해하면 생각보다 쉬움!!!
# dp 배열이 의미하는 것 : i원을 만드는 방법의 수
# 만약 1원짜리로 1~10원을 만들려면? 각각 1가지 방법임
# 2원짜리로 1~10원을 만들려면? 1원은 만들 수 없음 -> 2원부터 시작
#   2원 만드는 방법: 1가지(2), 3원 만드는 방법: 1원 만드는 방법(1)에 2원을 더하면 됨 -> dp[3] += dp[1]
# => 일반화하면? dp[x] += dp[x-coin]
# 이걸 coin -> value 순으로 반복문 돌리면 된다!

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for val in range(coin, k+1):
        if coin > val:
            break
        if val == coin:
            dp[val] += 1
        else:
            dp[val] += dp[val-coin]

print(dp[k])