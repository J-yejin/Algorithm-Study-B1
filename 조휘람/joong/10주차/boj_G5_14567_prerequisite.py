import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
result = [1] * (N + 1)
while q:
    current = q.popleft()
    for n_h in graph[current]:
        indegree[n_h] -= 1
        result[n_h] = result[current] + 1
        
        if indegree[n_h] == 0:
            q.append(n_h)
for i in range(1, N + 1):
    print(result[i], end=' ')
        
        
    