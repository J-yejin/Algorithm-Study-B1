## 접근방법 : 위상정렬! - 순서가 정해진 요소들 사이의 정렬
# heap?
import sys
from heapq import heappop, heappush

input = sys.stdin.readlines()

N, M = map(int, input[0].split())

in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, M+1):
    u, v = map(int, input[i].split())
    graph[u].append(v)
    in_degree[v] += 1

heap = []
for i in range(1, N+1):
    if in_degree[i] == 0:
        heappush(heap, i)
order_ls = []

while heap:
    node = heappop(heap)
    order_ls.append(node)
    if graph[node]:
        for n in graph[node]:
            in_degree[n] -=1
            if in_degree[n] == 0:
                heappush(heap, n)

print(*order_ls)