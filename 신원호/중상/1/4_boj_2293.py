# 재귀로는 불가능...
# recursion error가 발생했을 때는 sys로 재귀 제한을 늘리기보다 다른 알고리즘을 탐색해볼 것


# dp
n, k = map(int, input().split())
dp = [0] * (k + 1)
# 0원을 만드는 것도 동전을 쓰지 않는다는 1가지 경우의 수
dp[0] = 1
coins = []
for _ in range(n):
    coins.append(int(input()))
# 동전 정렬 불필요

for coin in coins:
    # 2-n 타일링 참조
    # i를 만드는 경우의 수는 i-n를 만드는 경우의 수에 n짜리 동전을 추가하는 것을 포함
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
print(dp[k])