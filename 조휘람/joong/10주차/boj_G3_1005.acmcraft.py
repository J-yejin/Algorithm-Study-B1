import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for test_cast in range(T):
    N, K = map(int, input().split())

    time = [*map(int, input().split())]

    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        indegree[Y] += 1
    win = int(input())
    q = deque()
    result = []
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i-1]
    while q:
        current = q.popleft()
        result.append(current)
        for n_t in graph[current]:
            indegree[n_t] -= 1
            dp[n_t] = max(dp[n_t], dp[current]+time[n_t-1])
            if indegree[n_t] == 0:
                q.append(n_t)
                
    print(dp[win])
        