import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [-1] * 100001

q = deque([(N,0)])
visited[N] = 0

while q:
    cur, time = q.popleft()
    
    if cur == K:
        print(time)
        break
        
    for next_cur in [cur + 1, cur - 1, cur * 2]:
        if 0 <= next_cur < 100001:
            if visited[next_cur] == -1 or visited[next_cur] == time + 1:
                if next_cur == cur * 2:
                    visited[next_cur] = time
                    q.appendleft((next_cur, visited[next_cur]))
                else:
                    visited[next_cur] = time + 1
                    q.append((next_cur, visited[next_cur]))
                    
                
                
                