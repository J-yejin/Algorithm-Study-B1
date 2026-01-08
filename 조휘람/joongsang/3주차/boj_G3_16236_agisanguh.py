import sys
from collections import deque
from heapq import heappop, heappush
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

N = int(input())

space = [[*map(int, input().split())] for _ in range(N)]

d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
size = 2

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            shark_x, shark_y = j, i
            space[i][j] = 0
res = 0
cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((shark_y, shark_x, 0))
    visited[shark_y][shark_x] = 1
    food = []
    
    while q:
        y, x, dist = q.popleft()
        if food and dist > food[0][0]:
            break
        
        for dy, dx in d:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= ny <N and not visited[ny][nx]:
                if space[ny][nx] <= size:
                    visited[ny][nx] = 1
                    q.append((ny, nx, dist + 1))
                    
                    if 0 < space[ny][nx] < size:
                        heappush(food, (dist + 1, ny, nx))
    if food:
        now_dist, now_y, now_x = heappop(food)
        
        shark_x = now_x
        shark_y = now_y
        space[shark_y][shark_x] = 0
        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0
        res += now_dist
        visited[shark_y][shark_x] = 1

    else:
        break
print(res)
