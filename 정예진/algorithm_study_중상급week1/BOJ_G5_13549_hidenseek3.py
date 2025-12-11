# 접근 방법 : 앞선 문제에서 시간만 구하면 됨 + 순간이동 시 걸리는 시간 0초로 이동 방법이 달라짐
# -> 0–1 BFS(가중치가 0과 1인 최단 거리 문제) 라고 합니다
# 0-1 BFS의 규칙
# - 가중치 0인 간선은 큐의 앞쪽에 넣는다. (더 먼저 탐색해야 함)
# - 가중치 1인 간선은 큐의 뒤쪽에 넣는다.
# => 이걸 구현해서 time 리스트로 해당 위치에 도달하기 위한 최단 시간 구함

from collections import deque

N, K = map(int, input().split())

MAX = 100000

time = [float('inf')] * (MAX+1)  # 타임을 -1이 아니라 무한대로 설정한 이유는 0초 순간이동 방법 때문!
# 이미 방문한 곳이라도 더 짧은 시간으로 다시 방문할 수 있음, 0초 순간이동 때문에 더 빠른 경로가 나중에 발견될 수도 있음!!
# 최단 시간을 구하기 위해서는 최솟값 비교가 필요하기 때문에 inf로 초기화 (이것도 원래처럼 -1로 했다가 gpt 힌트 받고 바꿨어요)

q = deque([N])
time[N] = 0

while q:
    now = q.popleft()
    next = now * 2
    if 0<=next<=MAX and time[next]>time[now]:  # 이 조건 못 찾아서.. 정말 오래 고민하다가 결국 gpt한테 힌트 받았어요 ㅜ
        time[next] = time[now]                 # next까지 걸린 시간이 now까지 걸린 시간보다 클 때만 갱신하면 됨! 같거나 적으면 필요 X
        q.appendleft(next)                     # 0초 이동은 왼쪽에 넣어서 먼저 처리

    for next in (now+1, now-1):
        if 0 <= next <= MAX and time[next]>time[now]+1:  # 여기도 마찬가지로 next까지 걸린 시간이 더 오래걸릴 때만 갱신!
            time[next] = time[now] + 1
            q.append(next)                     # 1초 이동은 오른쪽에 넣어서 나중에 처리

print(time[K])

