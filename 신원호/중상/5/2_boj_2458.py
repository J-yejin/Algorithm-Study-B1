# boj 2458 키 순서
# dijkstra 응용 - 플로이드-워셜?

import sys
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

# taller[i][j] == True: i보다 j가 키가 크다는 것이 자명함.
# 즉, taller[i][j]와 taller[j][i] 중 하나가 True라면 두 학생 간의 상하간계가 정립되어 있음
# 상하관계가 정립된 학생 수가 N - 1이라면 (본인을 제외한 전원) 본인의 키 순서를 확실히 알고 있는 상태
taller = [[False] * (N + 1) for _ in range(N + 1)]
for student in range(1, N + 1):
    q = deque([student])
    while q:
        now = q.popleft()
        for target in graph[now]:
            if taller[student][target]:
                continue
            taller[student][target] = True
            q.append(target)

result = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if taller[i][j]:
            count += 1
        elif taller[j][i]:
            count += 1
    if count == N - 1:
        result += 1
print(result)