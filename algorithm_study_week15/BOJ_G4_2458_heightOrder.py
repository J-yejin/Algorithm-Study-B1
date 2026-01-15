# 접근법 : 1) 플로이드 워셜 : 3중 for 문 돌아서 특정 비교 사이에 어떤 노드가 있는지 확인 -> python으로 하면 시간초과 남 터짐
# 그래서 새로운 방법 고민중
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

ans = 0

for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if graph[i][j] == 1 or graph[j][i] == 1:
            cnt += 1

    if cnt == N-1:
        ans += 1

print(ans)