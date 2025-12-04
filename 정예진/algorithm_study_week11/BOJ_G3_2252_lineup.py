## 접근방법 : 위상정렬! - 순서가 정해진 요소들 사이의 정렬
# https://seanpark11.tistory.com/131 참고해서 코드 구성
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
order_ls = []

while queue:
    node = queue.popleft()
    order_ls.append(node)
    if graph[node]:
        for n in graph[node]:
            in_degree[n] -=1
            if in_degree[n] == 0:
                queue.append(n)

print(*order_ls)