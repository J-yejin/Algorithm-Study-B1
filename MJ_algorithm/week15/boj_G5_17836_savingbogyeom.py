import sys  

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

q = deque([(0,0)])
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited[0][0] = 1

gram_dist = 10**10

while q:
    x, y = q.popleft()

    if x == N-1 and y == M-1 : 
        gram_dist = min(visited[x][y] - 1, gram_dist)

    if board[x][y] == 2 :
        temp_dist = (visited[x][y] - 1) + (N-1 - x) + (M-1 - y)
        gram_dist = min(gram_dist, temp_dist)

    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:

            if board[nx][ny] != 1:
                    
                    visited[nx][ny] = visited[x][y] + 1 #1초
                    q.append((nx, ny))
        

if gram_dist > T:
    print("Fail")
else:
    print(gram_dist)