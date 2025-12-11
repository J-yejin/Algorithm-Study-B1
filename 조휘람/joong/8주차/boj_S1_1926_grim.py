import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

lst = [[*map(int, input().split())] for _ in range(N)]
#상하좌우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[0]*M for _ in range(N)]

cnt = 0
max_size = 0
for y in range(N):
    for x in range(M):
        if lst[y][x] == 1 and not visited[y][x]:
            cnt += 1       
            visited[y][x] = 1
            current_area = 1   
            
            q = deque()
            q.append((y, x))
            
            while q:
                sy, sx = q.popleft()
                for dy, dx in d:
                    ny = sy + dy
                    nx = sx + dx
                    if 0 <= ny < N and 0 <= nx < M:
                        if lst[ny][nx] == 1 and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            current_area += 1
                            q.append((ny, nx))
            
            max_size = max(max_size, current_area)

print(cnt)
print(max_size)