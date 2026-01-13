import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
print(graph)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
print(graph)

def recur():
    pass