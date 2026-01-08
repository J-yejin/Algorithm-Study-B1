import sys
from collections import deque

N, K = map(int, input().split())
result = [100000, 0]    # [최소 시간, 경로 수]
# BFS
visited = [False] * 100001
visited[N] = True
route = deque([(N, 0)])
while route:
    now, time = route.popleft()
    # 가지치기
    if time > result[0]:
        continue
    # result 갱신
    if now == K:
        if time < result[0]:
            result[0] = time
            result[1] = 1
        elif time == result[0]:
            result[1] += 1
        continue
    visited[now] = True
    # 같은 시간이 소요되더라도 이동 경로가 다르다면 다른 결과로 취급하기 때문에
    # visited를 갱신하는 것은 큐에 넣을 때가 아닌 큐에서 뺄 때
    if now * 2 <= 100000 and not visited[now * 2]:
        route.append((now * 2, time + 1))
    if now - 1 >= 0 and not visited[now - 1]:
        route.append((now - 1, time + 1))
    if now + 1 <= 100000 and not visited[now + 1]:
        route.append((now + 1, time + 1))
print(result[0])
print(result[1])