import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    buildtime = [0] + list(map(int, input().split()))

    buildorder = [[] for _ in range(N+1)]

    order = [0] * (N+1)

    for _ in range(K):
        a, b = map(int, input().split())
        buildorder[a].append(b)
        order[b] += 1

    W = int(input())

    q = deque()
    
    elapsedTime = [0] * (N+1)
    
    for i in range(1, N+1):
        if order[i] == 0 :
            q.append(i)
            elapsedTime[i] = buildtime[i]

    while q:
        cur_building = q.popleft()
        
        for next_building in buildorder[cur_building]:
            order[next_building] -= 1
            if order[next_building] == 0 :
                q.append(next_building)
            elapsedTime[next_building] = max(elapsedTime[next_building], elapsedTime[cur_building] + buildtime[next_building])

    print(elapsedTime[W])

    