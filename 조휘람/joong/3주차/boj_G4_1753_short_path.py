import sys
input = sys.stdin.readline
from heapq import heappop, heappush
V, E = map(int,input().split())
start = int(input())
arr = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, input().split())
  arr[u].append((w, v))
INF = float('inf')
def dijkstra(start):
  dist = [INF] * (V + 1)
  pq = []
  dist[start] = 0
  heappush(pq,(0, start))
  
  while pq:
    cost, u = heappop(pq)
    if cost > dist[u]:
      continue
    for w, v in arr[u]:
      if dist[v] > cost + w:
        dist[v] = cost + w
        heappush(pq, (dist[v], v))
  return dist
    
for i in dijkstra(start)[1:]:
  if i == INF:
    print('INF')
  else:  
    print(i)
    

