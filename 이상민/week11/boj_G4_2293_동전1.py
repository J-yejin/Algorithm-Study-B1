N, K = map(int,input().split())
W = sorted(int(input()) for _ in range(N))
D = [0]*(K+1)

for w in W:
    if w > K: break
    D[w]+=1
    for i in range(w+1,K+1):
        D[i]+=D[i-w]

print(D[K])