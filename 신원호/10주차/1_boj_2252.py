# boj 2252 줄 세우기
# 위상 정렬에 대해 배울 수 있는 문제
# 2458번 키 순서 문제에서 진입, 진출 차수에 대한 아이디어를 써 본적이 있어서 풀이가 수월했다
# 이후 찾아보니 bfs를 사용하는 방법 말고 dfs를 사용하는 방법도 있다고 함

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
taller_than = [0] * (N + 1)
heights = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    taller_than[b] += 1
    heights[a].append(b)

checked = [False] * (N + 1)
q = deque([])
for i in range(1, N + 1):
    if taller_than[i] == 0:
        q.append(i)
        checked[i] = True

result = []
while q:
    node = q.popleft()
    for taller in heights[node]:
        taller_than[taller] -= 1
        if taller_than[taller] == 0:
            q.append(taller)
            checked[taller] = True
    result.append(node)

print(*result)

