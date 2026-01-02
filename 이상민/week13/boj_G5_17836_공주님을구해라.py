from collections import deque

N,M,T = map(int,input().split())

B = [[*map(int,input().split())] for _ in range(N)]

DR = [1,-1,0,0]
DC = [0,0,1,-1]

Q = deque()
Q.append((0,0))

V = [[-1]*M for _ in range(N)]
V[0][0] = 0

while Q:
    r,c = Q.popleft()
    for i in range(4):
        r_next,c_next = r+DR[i],c+DC[i]
        if r_next<0 or r_next>=N or c_next<0 or c_next>=M or V[r_next][c_next]>=0 or B[r_next][c_next]==1: continue
        V[r_next][c_next] = V[r][c]+1
        Q.append((r_next,c_next))

path1 = V[N-1][M-1]

for r in range(N):
    for c in range(M):
        if B[r][c] == 2:
            if V[r][c]<0: path2 = -1
            else: path2 = N+M-r-c-2+V[r][c]

if not(0<path1<=T) and not(0<path2<=T): print('Fail')
else: print(min(path1 if path1>0 else T,path2 if path2>0 else T))