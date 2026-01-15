import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

INF = 10**18
dist = [INF] * (N + 1)
dist[1] = 0 

for _ in range(N - 1):
    for u, v, w in graph:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

cycle = False
for u, v, w in graph:
    if dist[u] != INF and dist[u] + w < dist[v]:
        cycle = True
        break

if cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        if dist[i] != INF:
            print(dist[i])
        else:
            print(-1)
