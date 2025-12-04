import sys
from collections import deque

input = sys.stdin.readlines()

N, M = map(int, input[0].split())

in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, M+1):
    u, v = map(int, input[i].split())
    graph[u].append(v)
    in_degree[v] += 1

queue = deque([i for i in range(1, N+1) if in_degree[i] == 0])
semester = [1] * N

while queue:
    node = queue.popleft()
    if graph[node]:
        for n in graph[node]:
            in_degree[n] -=1
            semester[n-1] = semester[node-1] + 1
            # 기본 위상정렬과 다른 점: 다음 노드의 진입 차수를 깎아줄 때 해당 노드까지 도달할 수 있는 거리를 1씩 더해준다
            if in_degree[n] == 0:
                queue.append(n)

print(*semester)