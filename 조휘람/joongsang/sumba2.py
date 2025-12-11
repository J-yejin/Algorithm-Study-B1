from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
res_count = 0
res_time = 0

visited = [-1] * 100001
q = deque([(N, 0)])
visited[N] = 0
while q:
    cur, time = q.popleft()
    
    if res_count > 0 and time > res_time:
        break
    
    if cur == K:
        if res_count == 0:
            res_time = time
            res_count += 1
        elif time == res_time:
            res_count += 1
        continue
    
    for next_cur in [cur - 1, cur + 1, cur * 2]:
        if 0 <= next_cur < 100001:
            if visited[next_cur] == -1 or visited[next_cur] == time + 1:
                visited[next_cur] = time + 1
                q.append((next_cur, visited[next_cur]))
print(res_time)
print(res_count)

