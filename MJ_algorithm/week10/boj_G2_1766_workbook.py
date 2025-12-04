import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())

guide = [[] for _ in range(N+1)]

order = [0]  * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    guide[a].append(b)
    order[b] += 1

# print(guide[1:])
# print(order[1:])

q = [] #우선순위큐

for i in range(1, N+1):
    if order[i]==0:
        heapq.heappush(q, i)
       

result = []

while q:
    cur_question = heapq.heappop(q)
    result.append(cur_question)

    for next_question in guide[cur_question]:
        
        order[next_question] -= 1
        if order[next_question] == 0:
            heapq.heappush(q, next_question)
        
print(result)