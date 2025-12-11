import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().splilt())
    graph[a].append(b)