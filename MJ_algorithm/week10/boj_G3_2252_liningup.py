import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())

students = [[] for _ in range(N+1)]

order = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    students[a].append(b)
    order[b] += 1

print(students, order)

q = deque()

for i in range(1, N+1):
    if order[i] == 0 :
        q.append(i)
    
result = []

while q:
    cur_student = q.popleft()
    for student in students[cur_student]:
        order[student] -= 1
        if order[student] == 0 :
            q.append(student)
    
    result.append(cur_student)

    

    print(order)
print(result)