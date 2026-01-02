import sys
sys.stdin = open('input.txt', 'r')

import sys
from collections import deque


# 0-1 bfs
# SWEA 스노우 브라더스도 이 방식으로 풀 수 있을 듯?
N, K = map(int, input().split())
MAX = 100000
visited = [0] * (MAX + 1)
visited[N] = 1
route = deque([(N, 0)])
while route:
    now, time = route.popleft()
    if now == K:
        print(time)
        break
    # 최소 시간만 구하는거니까 visited는 큐에 넣을 때 갱신
    # 순간이동 쪽이 최소시간을 구하는 쪽에 유리, 따라서 appenleft하기
    if now * 2 <= MAX and not visited[now * 2]:
        route.appendleft((now * 2, time))
        visited[now * 2] = 1
    if now - 1 >= 0 and not visited[now - 1]:
        route.append((now - 1, time + 1))
        visited[now - 1] = 1
    if now + 1 <= MAX and not visited[now + 1]:
        route.append((now + 1, time + 1))
        visited[now + 1] = 1