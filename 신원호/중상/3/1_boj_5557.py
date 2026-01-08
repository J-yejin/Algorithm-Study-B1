# boj 5557 1학년

import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
# 2차원 배열 dp
# dp[i][j]: i번째 숫자까지 사용했을 때 j를 계산결과로 반환하는 경우의 수
dp = [[0] * 21 for _ in range(N - 1)]
dp[0][nums[0]] = 1
for i in range(1, N - 1):
    num = nums[i]
    for j in range(21):
        if j - num >= 0:
            dp[i][j] += dp[i - 1][j - num]
        if j + num <= 20:
            dp[i][j] += dp[i - 1][j + num]
print(dp[N - 2][nums[N - 1]])