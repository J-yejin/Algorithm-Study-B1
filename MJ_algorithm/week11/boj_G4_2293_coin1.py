import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

# print(coins)

dp = [0] * (k+1)

dp[0] = 1  #0원을 만드는 경우의 수


#1원을 만드는 경우의 수 = 1 
#2원을 만드는 경우의 수 = 1원 2개로 2원 만들기 + 2원 1개 쓰고 잔액(이 경우 0원)을 1원짜리로 만들기
#3원을 만드는 경우의 수 = 1원 3개로 3원을 만들기 + 2원 1개 쓰고 잔액(이 경우 1원)을 1원짜리로 만들기
#4원 = 1원 4개 + 2원 1개 쓰고 , 이때 남은 2원을 또 만드는 경우의 수(dp[2])

#8원 = 1원 8개 / 2원 1개 쓰고 남은 6원(dp[6]) / 2원 2개 쓰고 남은 4원

for coin in coins:
    for i in range(1, k+1):
        if i < coin :   #3원을 만들 때 3원보다 비싼 5원짜리동전은 고려하지 않도록
            continue
        dp[i] += dp[i - coin]

# print(dp)
print(dp[k])
