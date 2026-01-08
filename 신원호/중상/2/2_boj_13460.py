from collections import deque

# 구현 문제에서 구현해야 할 동작이 많거나 복잡해진다면 여러개의 함수로 쪼개보자

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 단일 구슬의 움직임
# sy, sx에서 출발한 구슬이 direction 방향으로 기울였을 때
# 몇칸 움직여서 어디로 도착하는가
def move(sy, sx, direction):
    count = 0
    ny, nx = sy, sx
    dy, dx = delta[direction]
    # 움직일 위치가 벽이 아니고, 현재 위치가 구멍이 아니라면
    while maps[ny + dy][nx + dx] != '#' and maps[ny][nx] != 'O':
        ny += dy
        nx += dx
        count += 1
    return ny, nx, count


# red, blue와 구멍 간의 상호작용을 고려한 움직임
def gravity(direction, red_start, blue_start):
    y_red, x_red = red_start
    y_blue, x_blue = blue_start
    dy, dx = delta[direction]

    ny_red, nx_red, count_red = move(y_red, x_red, direction)
    ny_blue, nx_blue, count_blue = move(y_blue, x_blue, direction)

    # 두 구슬의 위치가 같은 경우
    # 한 구슬이 다른 구슬을 가로막았거나 두 구슬이 모두 구멍에 빠졌거나
    # 구슬끼리 가로막은 경우만 위치를 보정해준다
    if (ny_red, nx_red) == (ny_blue, nx_blue) and maps[ny_red][nx_red] != 'O':
        if count_red > count_blue:
            ny_red -= dy
            nx_red -= dx
        else:
            ny_blue -= dy
            nx_blue -= dx
    return (ny_red, nx_red), (ny_blue, nx_blue)

# bfs
def solve():
    q = deque([(red, blue, 0)])
    # 진행 턴과는 무관하게 각 구슬들의 위치를 memoization에 기록
    memoization = set((red, blue))
    while q:
        now_red, now_blue, turn = q.popleft()
        for d in range(4):
            d_red, d_blue = gravity(d, now_red, now_blue)
            # red와 blue의 위치가 같을 경우는 동시에 구멍에 도착한 경우
            if d_red == d_blue:
                continue
            # 움직임이 발생하지 않은 경우 가지치기
            if now_red == d_red and now_blue == d_blue:
                continue
            # blue만 구멍에 도착한 경우
            if maps[d_blue[0]][d_blue[1]] == 'O':
                continue
            # red만 구멍에 도착한 경우, 정답 반환
            if maps[d_red[0]][d_red[1]] == 'O':
                return turn + 1
            # 이미 확인한 위치 기록일 경우
            if (d_red, d_blue) in memoization:
                continue
            memoization.add((d_red, d_blue))
            # 현재 9턴 이상인 경우 이후 움직일 수 없으므로
            if turn < 9:
                q.append((d_red, d_blue, turn + 1))

    return -1


N, M = map(int, input().split())
maps = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        if maps[y][x] == 'O':
            hole = (y, x)
        elif maps[y][x] == 'R':
            red = (y, x)
        elif maps[y][x] == 'B':
            blue = (y, x)

print(solve())