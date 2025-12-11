from heapq import heappop, heappush

N,K = map(int,input().split())

V = {N,}

D = [0]*100001

Q = []
heappush(Q,(0,N))

while Q:
    d,q = heappop(Q)
    if q == K: break
    dq = q*2
    while 0<=dq<=100000 and dq not in V:
        D[dq]=d
        V.add(dq)
        heappush(Q,(d,dq))
        dq *= 2
    if q>0 and q-1 not in V:
        D[q-1]=d+1
        V.add(q-1)
        heappush(Q,(d+1,q-1))
    if q<100000 and q+1 not in V:
        D[q+1]=d+1
        V.add(q+1)
        heappush(Q,(d+1,q+1))

print(D[K])
