import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# print(graph)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
# print(graph)

cnt = [0] * (N + 1)

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    visited[i] = 1
    
    q = [i]
    while q:
        cur = q.pop()
        for ne in graph[cur]:
            if not visited[ne]:
                visited[ne] = 1
                q.append(ne)
                
                cnt[i] += 1
                cnt[ne] += 1
            
res = 0
for i in range(1, N + 1):
    if cnt[i] == N - 1:
        res += 1
        
print(res)
            