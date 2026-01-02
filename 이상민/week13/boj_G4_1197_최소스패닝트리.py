from heapq import heappop, heappush

N,E = map(int,input().split())

V = [0]*(N+1)

P = [[] for _ in range(N+1)]

for _ in range(E):
    r,c,w = map(int,input().split())
    P[r].append((w,c))
    P[c].append((w,r))

Q = []
heappush(Q,(0,1))

Res = 0

while Q:
    weight, node = heappop(Q)
    if V[node]: continue
    V[node] = 1
    Res += weight
    for weight_next, node_next in P[node]:
        if V[node_next]: continue
        heappush(Q,(weight_next,node_next))

print(Res)
