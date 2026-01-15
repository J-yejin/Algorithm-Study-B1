import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1


ans = 0

for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        if i == j: 
            continue

        if graph[i][j] == 1 or graph[j][i] == 1:
            count += 1

    if count == N - 1:
        ans += 1

print(ans)