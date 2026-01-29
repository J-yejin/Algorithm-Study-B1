# boj 11657 타임머신

import sys

# 음수의 가중치가 존재하는 최단 거리 문제
# 벨만-포드 알고리즘
N, M = map(int, input().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
INF = float('inf')
distance = [INF] * (N + 1)

def BF(s=1):
    distance[s] = 0
    for i in range(N):
        for start, end, weight in edges:
            nxt_dist = distance[start] + weight
            if distance[start] != INF and distance[end] > nxt_dist:
                distance[end] = nxt_dist
                if i == N - 1:
                    # 음수 사이클이 존재한다.
                    return True
    # 음수 사이클이 존재하지 않는다.
    return False

exist_negative_cycle = BF()

if exist_negative_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])