import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
for _ in range(M):
    lst = [*map(int, input().split())]
    for i in range(1, len(lst)-1):
        graph[lst[i]].append(lst[i + 1])
        indegree[lst[i+1]] += 1
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

if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)
    
    