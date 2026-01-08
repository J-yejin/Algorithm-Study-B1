import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = []
for _ in range(E):
    s, e, v = map(int, input().split())
    graph.append((v, s, e))
graph.sort()

parents = [i for i in range(V + 1)]
rank = [0] * (V + 1)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    
    if rank[a] < rank[b]:
        parents[a] = b
    elif rank[b] < rank[a]:
        parents[b] = a
    else:
        parents[b] = a
        rank[a] += 1
res = 0
cnt = 0

for v, s, e in graph:
    if find(s) != find(e):
        union(s, e)
        res += v
        cnt += 1
        
    if cnt == V - 1:
        break
print(res)
        

    