import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

build_time = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for i in range(1, N + 1):
    data = list(map(int, input().split()))

    build_time[i] = data[0]

    # 나머지는 선행 건물들 (마지막 -1 제외)
    for x in data[1:-1]:
        graph[x].append(i)
        in_degree[i] += 1

dp = build_time[:]  # 자기 자신 건설 시간으로 초기화
queue = deque()

# 진입차수 0인 건물 큐에 넣기
for i in range(1, N + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    for n in graph[node]:
        in_degree[n] -= 1
        dp[n] = max(dp[n], dp[node] + build_time[n])
        if in_degree[n] == 0:
            queue.append(n)

for i in range(1, N + 1):
    print(dp[i])