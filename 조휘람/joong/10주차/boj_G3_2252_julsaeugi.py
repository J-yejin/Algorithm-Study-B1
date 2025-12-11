import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N +1)



for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1
    
q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
result = []

while q:
    current = q.popleft()
    result.append(current)
    
    for n_h in graph[current]:
        indegree[n_h] -= 1
        
        if indegree[n_h] == 0:
            q.append(n_h)
print(*result)