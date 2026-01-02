n, k = map(int, input().split())
coins = set()
# 중복 동전이 존재할 수 있으므로 세트 사용
for _ in range(n):
    coins.add(int(input()))
coins = list(coins)

# k가 10000 이하, 동전의 가치가 최소 1이므로 MAX 개수는 10000
MAX = 10001
dp = [MAX] * (k + 1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k + 1):
        # 금액 i를 만드는 동전 개수의 최소치
        # 현재의 최소치 dp[i]와 현재 선택된 동전을 쓰는 경우 dp[i - coin] + 1 중 작은 쪽
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 인라인으로 써보고 싶었음
print(-1 if dp[k] == MAX else dp[k])