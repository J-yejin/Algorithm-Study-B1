# 접근방법 : BFS + 검 조건 어떻게 넣는지가 너무 어려웠음
# 처음 생각한 건 검을 먹으면 sword변수를 true로 변환해서 그거 기반으로 벽 뚫고 가는 거 넣기! 였는데
# 변수 처리하려니까 생각보다 코드가 복잡해지는 것 같아서 패스 하기로 함
# 대신 검을 먹으면 이제 그때부턴 벽 신경 안 쓰고 그냥 뚫고 가도 된다는 사실을 깨달음
# => 그럼 그냥 검 먹은 순간부터 바로 직선 거리 구하면 되겠구나!

import sys
from collections import deque
input = sys.stdin.readline

N,M,T = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))  # 용사 초기 위치

    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    gram_dist = float('inf')  # 그람(검)을 먹고 가는 경우의 거리 따로 처리 -> 동시에 처리하기 빡셈

    while q:
        x, y = q.popleft()

        # 검 없이 도착점
        if x == N - 1 and y == M - 1:
            # 검을 써서 온 거리(gram_dist)와 그냥 온 거리 중 최솟값
            return min(visited[x][y] - 1, gram_dist)

        # 그람(검)을 찾은 경우
        if map[x][y] == 2:
            # 여기까지 온 거리 + 도착점까지의 직선 거리 (벽 무시 가능하므로) - 이거 생각하는게 오래 걸림
            # (N-1, M-1)이 도착점 좌표
            temp_dist = (visited[x][y] - 1) + (N - 1 - x) + (M - 1 - y)
            gram_dist = temp_dist
        
        # 둘 다 아니면 상하좌우 순환
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았고, 벽이 아닌 경우
                if visited[nx][ny] == 0 and map[nx][ny] != 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

    # 만약 큐가 빌 때까지 도착점에 못 갔다면, 그람을 먹은 경우라도 반환
    return gram_dist


result = bfs()

if result > T:
    print('Fail')
else:
    print(result)