import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N, M = map(int, input().split())

courses = [[] for _ in range(N+1)]
order = [0] * (N+1)

semester = [1] * (N+1)


for _ in range(M):
    a, b  = map(int, input().split())
    courses[a].append(b)
    order[b] += 1

# print(order)

q = deque()

for i in range(1, N+1):
    if order[i] == 0:
        q.append(i)


while q:
    cur_course = q.popleft()
    
    for next_course in courses[cur_course]:
        order[next_course] -= 1
        
        semester[next_course] = max(semester[next_course], semester[cur_course] +1)

        if order[next_course] == 0:
            q.append(next_course)
        
        
print(*semester[1:])        