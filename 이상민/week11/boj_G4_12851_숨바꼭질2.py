import sys

input = sys.stdin.read

N,K = map(int,input().split())

Q = {N,}
V = {N,}

R = 0
D = [0]*100001

D[N] = 1

while Q:
    if K in V: break
    v = set()
    for q in Q:
        if q>0 and q-1 not in V:
            D[q-1]+=D[q]
            v.add(q-1)
        if q<100000 and q+1 not in V:
            D[q+1]+=D[q]
            v.add(q+1)
        if q<=50000 and q*2 not in V:
            D[q*2]+=D[q]
            v.add(q*2)
    R+=1
    V|=v
    Q=v

print(R)
print(D[K])