import sys
sys.stdin = open('input.txt', 'r')

# boj 9370 미확인 도착지

import sys
import heapq

# start부터 모든 노드로의 최단 거리를 구하는 dijkstra
def dijkstra(start):
    visited = [MAX] * (n + 1)
    q = [(0, start)]
    while q:
        distance, now = heapq.heappop(q)
        if visited[now] > distance:
            visited[now] = distance
        for target in edges[now]:
            if visited[target[0]] <= distance + target[1]:
                continue
            heapq.heappush(q, (distance + target[1], target[0]))
    return visited

T = int(input())
MAX = float('inf')
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n + 1)]
    s, g, h = map(int, sys.stdin.readline().split())
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        edges[a].append((b, d))
        edges[b].append((a, d))
    candidate = sorted([int(sys.stdin.readline()) for _ in range(t)])
    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    result = []
    # 주의!! float('inf') == float('inf') + float('inf')
    for candy in candidate:
        if dist_s[candy] == MAX:
            continue
        if dist_s[candy] == dist_s[g] + dist_g[h] + dist_h[candy]:
            result.append(candy)
        elif dist_s[candy] == dist_s[h] + dist_h[g] + dist_g[candy]:
            result.append(candy)
    print(*result)