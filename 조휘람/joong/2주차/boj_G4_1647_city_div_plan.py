import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = []
for _ in range(M):
    u, v, c = map(int, input().split())
    graph.append((c, u, v))
graph.sort(key=lambda x:x[0])
cnt = 0
result = 0
parents = [i for i in range(N+1)]
max_w = 0

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]
def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return
    if rx < ry:
        parents[rx] = ry
    else:
        parents[ry] = rx
for w, u, v in graph:
    if find_set(u) != find_set(v):
        union(u, v)
        cnt += 1
        result += w
        max_w = max(w, max_w)
    if cnt == N - 1:
        break

print(result-max_w)