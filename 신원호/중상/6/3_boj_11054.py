N = int(input())
nums = list(map(int, input().split()))
LIS = [1] * N
for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            LIS[i] = max(LIS[j] + 1, LIS[i])
LDS = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] > nums[j]:
            LDS[i] = max(LDS[j] + 1, LDS[i])
result = []
for i in range(N):
    result.append(LIS[i] + LDS[i] - 1)
print(max(result))