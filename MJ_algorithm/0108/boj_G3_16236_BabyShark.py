import sys
from collections import deque


sys.stdin = open('input.txt', 'r')

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
print(board)

shark_size = 2
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_x, shark_y = i, j
            board[i][j] = 0    #중요.. 9로 놔두면 나중에 크기가 9인 물고기로 됨
        
dr = [-1,0,1,0] 
dc = [0,-1,0,1]

fish_count = 0
time = 0

def simulate(shark_x, shark_y):
    visited = [[-1] * N for _ in range(N)]
    q = deque([(shark_x, shark_y)])
    visited[shark_x][shark_y] = 0

    next_fishes = []
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            next_x, next_y = cur_x + dr[i], cur_y + dc[i]

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N :
                continue
            if visited[next_x][next_y] != -1 :
                continue

            if board[next_x][next_y] <= shark_size :
                visited[next_x][next_y] = visited[cur_x][cur_y] + 1  #(지나갈 수 있는 칸에 대해) 거리 정보 필요
                q.append((next_x, next_y))

                if 0 < board[next_x][next_y] < shark_size :  #지나갈 수만 있고 먹을 수는 없는 칸도 존재 (크기가 같을 때)
                    next_fishes.append((visited[next_x][next_y], next_x, next_y))

    if next_fishes:
        next_fishes.sort(key=lambda x: (x[0], x[1], x[2])) #거리, row값이 작은 순, column값이 작은 순
        return next_fishes[0]
    
    else:
        return []
    
while True:

    next_fish = simulate(shark_x, shark_y)

    if next_fish == []:
        break

    dist, next_x, next_y = next_fish  #next_fish가 존재햇으면 거기로 와서

    time += dist
    shark_x, shark_y = next_x, next_y  #상어위치 이동
    fish_count += 1  # 한마리 먹은거임
    board[next_x][next_y] = 0 


    if fish_count == shark_size :
        shark_size += 1
        fish_count = 0 #레벨업하면 경험치 초기화 



print(time)

