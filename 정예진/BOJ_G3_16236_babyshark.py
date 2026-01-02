import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]  # 공간

start_r, start_c = 0, 0  # 아기상어 위치

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            start_r, start_c = i, j
            space[i][j] = 0  # 처음에는 이거 안했다가 뒤에 가서 상어 이동할 때 귀찮아서 0으로 바꿈 (왜냐면 초기 위치 알면 더이상 필요 없음!)

size = 2
eat = 0  # 먹은 물고기의 수
time = 0 # 총 걸린 시간

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# BFS 함수 구현
def bfs(start_r, start_c, current_size):
    # 방문 여부 + 거리 저장할 배열
    visited = [[-1] * N for _ in range(N)]  # BFS 여러번 돌려야 하니까 함수 내에 정의

    # 시작 위치 설정
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 0  # 출발점은 거리가 0이니까

    # 먹을 수 있는 물고기 후보군 담을 리스트
    candidates = []

    while q:
        curr_r, curr_c = q.popleft()

        # 만약 이미 먹을 물고기 후보를 찾았는데, 현재 위치가 그 후보보다 멀다면 break
        if candidates and visited[curr_r][curr_c] >= candidates[0][0]:
            break

        for i in range(4):
            nx, ny = curr_r + dx[i], curr_c + dy[i]

            # 1. 범위 내에 있고 아직 방문하지 않았으며
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 2. 이동 가능 조건: 빈 칸(0)이거나, 내 크기보다 작거나 같은 물고기  -> 여기서 9가 거슬렸음 미리 처리해주기
                if space[nx][ny] <= current_size:
                    visited[nx][ny] = visited[curr_r][curr_c] + 1
                    q.append((nx, ny))

                    # 3. 먹기 가능 조건: 빈 칸이 아니고, 내 크기보다 작은 물고기
                    if 0 < space[nx][ny] < current_size:
                        # (거리, 행, 열) 순으로 저장 
                        candidates.append((visited[nx][ny], nx, ny))

    # 먹을 수 있는 물고기가 있다면 정렬 기준에 맞춰 정렬
    if candidates:
        # 정렬 우선순위: 1. 거리(작은순) 2. 행(위쪽) 3. 열(왼쪽)
        candidates.sort(key=lambda x: (x[0], x[1], x[2]))
        return candidates[0]  # 가장 우선순위 높은 물고기 정보 반환
    else:
        return None  # 먹을 수 있는 물고기가 없음


while True:
    # BFS로 먹을 물고기 탐색
    result = bfs(start_r, start_c, size)

    # 더 이상 먹을 물고기가 없으면 종료 (엄마 상어 호출)
    if result is None:
        print(time)
        break

    # 물고기를 먹은 경우 처리 -> 다시 BFS에 넣을 출발점
    dist, next_r, next_c = result

    # 1. 시간 추가
    time += dist

    # 2. 위치 이동 및 맵 갱신
    start_r, start_c = next_r, next_c
    space[next_r][next_c] = 0  # 물고기 먹었으니 빈 칸으로

    # 3. 경험치 처리
    eat += 1
    if eat == size:
        size += 1
        eat = 0