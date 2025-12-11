import sys

def find_giga(r):
    global res_1
    g = r
    if g == R and len(P[g])!=1: return g
    while g==R or len(P[g]) == 2:
        for n,dw in P[g]:
            if V[n]: continue
            V[n]=1
            res_1+=dw
            g = n
    return g

N,R,*L = map(int,sys.stdin.read().split())

P = [[]for _ in range(N+1)]

for s,e,w in zip(L[::3],L[1::3],L[2::3]):
    P[s].append((e,w))
    P[e].append((s,w))

res_1 = res_2 = 0

V = [0]*(N+1)
V[R]=1

G = find_giga(R)

S = []

for s,w in P[G]:
    S.append((s,w))
    V[s]=1

while S:
    s,w = S.pop()
    if len(P[s])==1:
        res_2 = max(res_2,w)
        continue
    for e,dw in P[s]:
        if V[e]:continue
        V[e]=1
        S.append((e,w+dw))

print(res_1,res_2)