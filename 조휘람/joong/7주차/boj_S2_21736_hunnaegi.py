import sys
from collections import deque

input = sys.stdin.readline
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]

N, M = map(int, input().split())
map = [list(input().strip()) for _ in range(N)]

for i in range(N):
	for j in range(M):
		if map[i][j] == 'I':
			start = (i, j)
			break
		
visited = [[0]*M for _ in range(N)]
q = deque([start])
visited[start[0]][start[1]] = 1

cnt = 0

while q:
    x, y = q.popleft()
    
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if not visited[nx][ny] and map[nx][ny] != 'X':
            visited[nx][ny] = 1
            if map[nx][ny] == 'P':
                cnt += 1
            q.append((nx, ny))
            
if cnt > 0:
    print(cnt)
else:
    print('TT')