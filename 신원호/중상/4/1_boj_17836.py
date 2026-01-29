# boj 17836 공주님을 구해라
# bfs
# visited 배열을 두 종류로 관리할 것
# 제한시간이 있으므로 조기 종료에 용이하게 함수 형태로 작성

import sys
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve():
    visited_normal = [[False] * M for _ in range(N)]
    visited_sword = [[False] * M for _ in range(N)]
    q = deque([(0, 0, 0, False)])
    while q:
        ny, nx, time, sword = q.popleft()
        for d1, d2 in delta:
            dy, dx = ny + d1, nx + d2
            if not (0 <= dy < N and 0 <= dx < M):
                continue
            if dy == N - 1 and dx == M - 1:
                if time + 1 <= T:
                    return time + 1
                else:
                    return 'Fail'
            if not sword:
                if visited_normal[dy][dx]:
                    continue
                if castle[dy][dx] == 1:
                    continue
                visited_normal[dy][dx] = True
            if sword:
                if visited_sword[dy][dx]:
                    continue
                visited_sword[dy][dx] = True

            if castle[dy][dx] == 2:
                q.append((dy, dx, time + 1, True))
            else:
                q.append((dy, dx, time + 1, sword))
    return 'Fail'


N, M, T = map(int, sys.stdin.readline().split())
castle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solve())