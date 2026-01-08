# boj 1197 최소 스패닝 트리

import sys
import heapq

sys.setrecursionlimit(10**6)

# 크루스칼(union-find) 알고리즘 사용
# setrecursionlimit 주의...

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
        return root[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        root[x] = y
    else:
        root[y] = x

V, E = map(int, sys.stdin.readline().split())
edges = []
root = list(range(V + 1))
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(edges, (c, a, b))
count = V - 1
result = 0
while count > 0:
    dist, a, b = heapq.heappop(edges)
    if find(a) == find(b):
        continue
    union(a, b)
    result += dist
    count -= 1
print(result)