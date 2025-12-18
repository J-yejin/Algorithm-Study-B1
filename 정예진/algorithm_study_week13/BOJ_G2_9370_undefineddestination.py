# 접근 방법 : 최단경로가 주어진 g-h를 지나도록 하는 문제, dijkstra + 조건 붙은거라고 생각하면 됨
# 중급에서 풀었던 문제 중 특정 지점을 지나가도록 하는 문제와 유사한 느낌
#
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
T = int(input())

def dijkstra(start):
    distances = [1e9] * (n+1)
    distances[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)

        if distances[now] < dist: # 이미 더 짧은 경로가 발견된 경우 무시
            continue

        for nxt in graph[now]:
            n_node, n_dist = nxt
            nxt_dist = dist + n_dist
            if nxt_dist < distances[nxt[0]]:
                distances[n_node] = nxt_dist
                heappush(q, (nxt_dist, n_node))
    return distances

for tc in range(T):
    # 교차로, 도로, 목적지 후보 개수
    n,m,t = map(int, input().split())
    # 예술가들의 출발지, 지나간 교차로의 양 끝 지점
    s,g,h = map(int, input().split())
    # m개의 줄에 a,b,d : a와 b 사이의 d 길이의 양방향 도로
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    arrive_can = []
    for _ in range(t):
        arrive_can.append(int(input()))

    dist_s = dijkstra(s) # 시작점으로부터 최단거리
    dist_g = dijkstra(g) # g로부터 최단거리
    dist_h = dijkstra(h) # h로부터 최단거리

    res = []

    for dest in arrive_can:
        total_dist = dist_s[dest]

        path1 = dist_s[g] + dist_g[h] + dist_h[dest]
        path2 = dist_s[h] + dist_h[g] + dist_g[dest]

        if total_dist == path1 or total_dist == path2:
            res.append(dest)
    print(*sorted(res))

