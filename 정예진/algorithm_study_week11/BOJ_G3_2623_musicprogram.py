## 접근방법 : 

import sys
from collections import deque

input = sys.stdin.readlines()

N, M = map(int, input[0].split())

in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(1, M+1):
    ls = list(map(int,input[i].split()))
    count, num_ls = ls[0], ls[1:]
    for idx in range(count-1):
        s, e = num_ls[idx], num_ls[idx+1]
        graph[s].append(e)
        in_degree[e] +=1

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

if len(order_ls) != N:
    print(0)
else:
    print(*order_ls, sep='\n')