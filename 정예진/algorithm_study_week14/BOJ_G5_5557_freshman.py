import sys

input = sys.stdin.readline

N = int(input())
all_nums = list(map(int, input().split()))

# 마지막 숫자는 등호 뒤의 수니까 따로 저장
nums = all_nums[:-1]  # 계산할 숫자들 (총 N-1개)
target = all_nums[-1]  # 최종적으로 만들어야 하는 수

# 2차원 DP 테이블
# 행(i): 몇 번째 숫자까지 썼는지 (0 ~ N-2)
# 열(j): 만들 수 있는 합계 (0 ~ 20)
dp = [[0] * 21 for _ in range(N - 1)]

# 첫 번째 숫자는 무조건 그 값 하나만 가능하니까 nums[0]에 1
dp[0][nums[0]] = 1

# nums의 개수만큼 순회
for i in range(1, N - 1):
    next_num = nums[i]  # 이번에 더하거나 뺄 숫자

    # j: 0부터 20까지 모든 칸을 확인
    for j in range(21):
        if dp[i - 1][j] > 0:
            # 1. 더하기
            plus_val = j + next_num
            if 0 <= plus_val <= 20: # 음수 X, 20 이상 X
                # dp[i-1][j]를 만드는 방법의 수를 누적해서 더해줌
                dp[i][plus_val] += dp[i - 1][j]

            # 2. 빼기
            minus_val = j - next_num
            if 0 <= minus_val <= 20:
                # dp[i-1][j]를 만드는 방법의 수를 누적해서 더해줌
                dp[i][minus_val] += dp[i - 1][j]

# 마지막 숫자까지 다 계산했을 때(N-2), 합이 target이 되는 경우의 수
print(dp[N - 2][target])