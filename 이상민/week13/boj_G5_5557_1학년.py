N = int(input())

B = [*map(int,input().split())]

V = [[0]*21 for _ in range(N-1)]
V[0][B[0]] = 1

for idx in range(N-2):
    for num in range(21):
        if not V[idx][num]: continue
        p,m = num+B[idx+1],num-B[idx+1]
        if 0<=p<=20: V[idx+1][p] += V[idx][num]
        if 0<=m<=20: V[idx+1][m] += V[idx][num]

print(V[N-2][B[-1]])