# 접근 방법 : queue으로 관리, 수빈이의 위치 N에서 K로 가는데 걸리는 시간(time)과 그 시간이 걸려서 도달할 수 있는 방법의 수(cnt)를 각각 관리
# 시간 배열(time)은 “최단 시간 기록”
# 카운트 배열(cnt)은 “해당 최단 시간의 경로 수 기록”
# 같은 시간으로 도착하는 경우만 cnt를 누적

from collections import deque

N, K = map(int, input().split())

MAX = 100000  # MAX는 있을 수 있는 위치의 최댓값 100000으로 설정

time = [-1] * (MAX+1)  # 시간은 0초가 걸릴 수도 있으니까 -1로 초기화, 방법은 0개로 초기화
cnt = [0] * (MAX+1)

q = deque([N])  # 시작 위치 queue에 넣어주기
time[N] = 0
cnt[N] = 1

while q:
    now = q.popleft()  # 현재 위치 뽑아내서
    for next in (now+1, now-1, now*2):  # 갈 수 있는 3가지 방법 순회
        if 0 <= next <= MAX:   # 범위 내에 있다면 (범위 내에 없으면 패스)
            if time[next] == -1:  # 아직 미방문한 곳이라면 -> 아직 방문한 적 없다는 것은 현재 시간이 최단 시간이라는 뜻
                time[next] = time[now] + 1    # 이동하는데 1초 걸리니까 time에 1초 추가
                cnt[next] = cnt[now]          # 이 위치에 오는 루트는 now와 next가 동일하니까 cnt는 같은 값으로 업데이트
                q.append(next)                # q에 next append

            elif time[next] == time[now] + 1:   # 만약 이미 다음 노드에 현재 노드에서 가는 것과 같은 시간으로 이미 방문한 적이 있다면
                cnt[next] += cnt[now]           # 또 다른 최단 경로를 하나 더 찾은 것! -> 가는 방법의 수 더해주기

print(time[K])
print(cnt[K])

