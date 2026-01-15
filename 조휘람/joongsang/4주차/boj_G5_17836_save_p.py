import sys
from collections import deque
input = sys.stdin.readline

d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

N, M, T = map(int, input().split())

castle = [[*map(int, input().split())] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if castle[i][j] == 2:
            gram_y = i
            gram_x = j
q = deque()
t = 1000000

q.append((0, 0, 0, False))
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
while q:
    y, x, n_t, n_h_gram = q.popleft()
    if y == N - 1 and x == M - 1:
        t = min(t, n_t)
        continue
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if n_h_gram:
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][1]:
                q.append((ny, nx, n_t + 1, n_h_gram))
                visited[ny][nx][1] = 1
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx][0]:
            nex_h_gram = False
            if castle[ny][nx] == 2:
                nex_h_gram = True
            if n_h_gram:
                q.append((ny, nx, n_t + 1, nex_h_gram))
                visited[ny][nx][1] = 1
            elif castle[ny][nx] == 1:
                continue
            else:
                if nex_h_gram:
                    q.append((ny, nx, n_t + 1, nex_h_gram))
                    visited[ny][nx][0] = 1
                q.append((ny, nx, n_t + 1, nex_h_gram))
                visited[ny][nx][0] = 1
                    
if t <= T:
    print(t)
else:
    print('Fail')
         
    