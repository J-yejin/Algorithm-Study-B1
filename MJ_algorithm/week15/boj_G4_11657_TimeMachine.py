import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())

graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

INF = 10**10
dist = [INF] * (N + 1)
dist[1] = 0

cycle = False

for i in range(N):
    for j in range(M):
        cur_node, next_node, cost = graph[j]
        
        if dist[cur_node] != INF and dist[cur_node] + cost < dist[next_node]:
            dist[next_node] = dist[cur_node] + cost
            
            if i == N - 1:
                cycle = True

if cycle:
    print("-1")
else:
    for i in range(2, N + 1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])