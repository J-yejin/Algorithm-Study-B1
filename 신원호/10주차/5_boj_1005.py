# boj 1005 ACM Craft
# 그래프의 간선에 가중치가 생겼다
# 1766번 문제와 마찬가지로 우선순위 큐를 사용하여 해겷하자

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

for _ in range(int(input())):
    N, K = map(int, input().split())
    build_time = [0] + list(map(int, input().split()))
    order_graph = [[] for _ in range(N + 1)]
    order_level = [0] * (N + 1)
    for _ in range(K):
        x, y = map(int, input().split())
        order_graph[x].append(y)
        order_level[y] += 1
    goal = int(input())
    q = []
    time = 0
    for i in range(1, N + 1):
        if order_level[i] == 0:
            heappush(q, (build_time[i], i))

    while q:
        n_time, build_num = heappop(q)
        if build_num == goal:
            print(n_time)
            break
        time = n_time
        for nxt in order_graph[build_num]:
            order_level[nxt] -= 1
            if order_level[nxt] == 0:
                heappush(q, (time + build_time[nxt], nxt))