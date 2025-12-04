# boj 1516 게임 개발
# 가중치가 있는 그래프 + 입력값 형식이 또 다르다
# 입력값에 주어지는 노드 번호는 진출하는 노드가 아닌 진입하는 노드임에 유의

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
graph = [[] for _ in range(N + 1)]
times = [0]
level = [0] * (N + 1)
for i in range(1, N + 1):
    time, *tech, __ = map(int, input().split())
    times.append(time)
    for num in tech:
        level[i] += 1
        graph[num].append(i)

q = []
for i in range(1, N + 1):
    if level[i] == 0:
        heappush(q, (times[i], i))

result = [0] * (N + 1)
timeline = 0
while q:
    time, build_num = heappop(q)
    timeline = time
    result[build_num] = time
    for nxt in graph[build_num]:
        level[nxt] -= 1
        if level[nxt] == 0:
            heappush(q, (timeline + times[nxt], nxt))

for i in range(1, N + 1):
    print(result[i])