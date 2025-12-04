import sys
from collections import deque
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())

order = [0] * (N+1)
singers = [[] for _ in range(N+1)]

for _ in range(M):
    input_list = list(map(int, input().split()))[1:]

    # print(input_list)
    for i in range(len(input_list)-1) : 
        a, b = input_list[i], input_list[i+1]
        singers[a].append(b)
        order[b] += 1

q = deque()
for i in range(1, N+1):
    if order[i] == 0:
        q.append(i)

result = []

while q:
    cur_singer = q.popleft()
    result.append(cur_singer)    
    
    for next_singer in singers[cur_singer]:
        order[next_singer] -= 1
    
        if order[next_singer] == 0 :
            q.append(next_singer)

    # print(q)
if len(result) != N :
    print(0)
else:
    print(*result)