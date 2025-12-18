from heapq import heappop, heappush

def dijkstra(num_node,start):
    Q = []
    W = [-1]*(num_node+1)
    heappush(Q,(0,start))
    while Q:
        w,n = heappop(Q)
        if W[n]>=0:continue
        W[n] = w
        for nn,dw in P[n]:
            if W[nn]>=0:continue
            heappush(Q,(w+dw,nn))
    return W

for test in range(int(input())):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())

    P = [[] for _ in range(n+1)]

    for _ in range(m):
        r,c,w = map(int,input().split())
        P[r].append((c,w))
        P[c].append((r,w))

    R = sorted(int(input()) for _ in range(t))

    WS = dijkstra(n,s)
    WG = dijkstra(n,g)
    WH = dijkstra(n,h)

    gh = WG[h]

    print( *[r for r in R if WS[r] == WS[g]+gh+WH[r] or WS[r] == WS[h]+gh+WG[r]])