import sys
from heapq import heappop, heappush
input = sys.stdin.readline
N, M, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
arr_r = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,c = map(int, input().split())
    arr[u].append((c, v))
    arr_r[v].append((c,u))

def dijkstra(n, graph, start):
    dist = [21e8] * (n+1)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        cost, u = heappop(pq)
        if cost > dist[u]:
            continue

        for w, v in graph[u]:
            if dist[v] > cost + w:
                dist[v] = cost + w
                heappush(pq, (dist[v], v))

    return dist
result = -21e8
for i in range(1, N+1):
    result = max(result, (dijkstra(N,arr,X)[i] + dijkstra(N,arr_r,X)[i]))
print(result)