import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)

    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        in_degree[Y] += 1

    W = int(input())

    queue = deque([i for i in range(1, N + 1) if in_degree[i] == 0])
    dp = build_time[:]
    order_ls = []

    while queue:
        node = queue.popleft()
        order_ls.append(node)
        for n in graph[node]:
            dp[n] = max(dp[n], dp[node] + build_time[n])
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)
    print(order_ls)

    print(dp[W])