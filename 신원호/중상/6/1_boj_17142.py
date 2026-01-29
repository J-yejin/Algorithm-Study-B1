import sys
from collections import deque

# bfs + dfs
# dfs로 활성 바이러스 조합을 구하고 bfs로 시뮬레이션

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def infect(select):
    q = deque(select)
    visited = [[-1] * N for _ in range(N)]
    for y, x in select:
        visited[y][x] = 0
    empty = remain
    time = 0
    while q:
        y, x = q.popleft()
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if lab[ny][nx] == 1:
                continue
            if visited[ny][nx] != -1:
                continue
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            if lab[ny][nx] == 0:
                empty -= 1
                time = visited[ny][nx]
    if empty > 0:
        return MAX
    return time

def solve(n=0, s=[], start=0):
    global result
    if n == M:
        result = min(result, infect(s))
        return
    for i in range(start, candidate):
        s.append(virus[i])
        solve(n + 1, s, i + 1)
        s.pop()

N, M = map(int, input().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus = []
remain = 0
for y in range(N):
    for x in range(N):
        if lab[y][x] == 2:
            virus.append((y, x))
        elif lab[y][x] == 0:
            remain += 1
candidate = len(virus)
MAX = float('inf')
result = MAX

solve()
print(-1 if result == MAX else result)