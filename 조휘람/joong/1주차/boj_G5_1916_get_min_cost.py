import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  s, e, c = map(int,input().split())
  graph[s].append((e,c))
start, end = map(int,input().split())
prev = [-1]*(N+1)
def dijkstra(n, graph, start):
  global prev
  dist = [21e8] * (n+1)
  prev = [-1] * (n+1)
  dist[start] = 0
  
  pq = [(0, start)]
  while pq:
    now_cost, now_mura = heappop(pq)
    if now_cost > dist[now_mura]:
      continue
    for next_mura, cost in graph[now_mura]:
      if dist[next_mura] > now_cost + cost:
        dist[next_mura] = now_cost + cost
        prev[next_mura] = now_mura
        heappush(pq, (dist[next_mura], next_mura))
  return dist[end]

dijkstra(N, graph, start)

def construct_path(prev, target):
  path = []
  cur = target
  while cur != -1:
      path.append(cur)
      cur = prev[cur]
  path.reverse()
  return path

print(construct_path(prev, 5))
print(dijkstra(N, graph, start))
        
 

