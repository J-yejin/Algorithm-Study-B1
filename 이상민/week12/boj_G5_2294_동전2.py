N, K = map(int,input().split())
W = [int(input()) for _ in range(N)]
D = [0]*(K+1)

for w in W:
    if w > K: continue
    D[w]=1
    for i in range(w+1,K+1):
        if D[i-w]:
            if D[i]: D[i]=min(D[i],D[i-w]+1)
            else: D[i]=D[i-w]+1


print(D[K] if D[K] else -1)