# boj 1766 문제집
# 2252번 문제와 거의 유사하나, 이 문제는 스페셜 저지가 없다!
# 위상 정렬 상 서열이 같다면, 낮은 번호를 우선 선택해야 하므로 우선순위 큐를 사용

import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
level = [0] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    level[b] += 1

q = []
for i in range(1, N + 1):
    if level[i] == 0:
        heappush(q, i)

result = []
while q:
    num = heappop(q)
    for nxt in graph[num]:
        level[nxt] -= 1
        if level[nxt] == 0:
            heappush(q, nxt)
    result.append(num)

print(*result)