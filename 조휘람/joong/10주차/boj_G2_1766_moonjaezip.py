import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
hq = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)
result = []
while hq:
    current = heapq.heappop(hq)
    result.append(current)
    for n_h in graph[current]:
        indegree[n_h] -= 1
        
        if indegree[n_h] == 0:
            heapq.heappush(hq, n_h)
print(*result)
    
    
    