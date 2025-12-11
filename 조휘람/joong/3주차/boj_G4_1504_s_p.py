import sys
from heapq import heappop, heappush 
input = sys.stdin.readline

N, E = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(E):
  u, v, c = map(int, input().split())
  arr[u].append((c, v))
  arr[v].append((c, u))
s1, s2 = map(int, input().split())

def dijkstra(n, arr, start):
  dist = [21e8] * (n + 1)
  dist[start] = 0
  pq = []
  heappush(pq, (0, start))
  while pq:
    cost, u = heappop(pq)
    if cost > dist[u]:
      continue
    for w, v in arr[u]:
      if cost + w <= dist[v]:
        dist[v] = cost + w
        heappush(pq, (dist[v], v))
  return dist
a1 = dijkstra(N, arr, 1)
a2 = dijkstra(N, arr, s1)
a3 = dijkstra(N, arr, s2)

path_s1 = a1[s1] + a2[s2] + a3[N]
path_s2 = a1[s2] + a3[s1] + a2[N]

if min(path_s1, path_s2) >= 21e8:
  result = -1
else: 
  result = min(path_s1, path_s2)
  
print(result)

