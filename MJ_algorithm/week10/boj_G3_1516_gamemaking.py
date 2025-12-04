import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())

buildtime = [0]

buildings = [[] for _ in range(N+1)]

order = [0] * (N+1)

for i in range(1, N+1):
    input_list = list(map(int, input().split()))
    buildtime.append(input_list[0])

    pre = input_list[1:-1]
    for _ in pre:
        buildings[_].append(i)
        order[i] += 1
# print(buildings)
# print(order)

elapsedtime = [0] * (N+1)

q = deque()
for i in range(1, N+1):
    if order[i] == 0:
        q.append(i)
        elapsedtime[i] = buildtime[i]

while q:
    cur_building = q.popleft()
    
    for next_building in buildings[cur_building]:
        order[next_building] -= 1
        if order[next_building] == 0:
            q.append(next_building)
        
        elapsedtime[next_building] = max(elapsedtime[next_building], elapsedtime[cur_building] + buildtime[next_building])

for _ in elapsedtime[1:]:
    print(_)