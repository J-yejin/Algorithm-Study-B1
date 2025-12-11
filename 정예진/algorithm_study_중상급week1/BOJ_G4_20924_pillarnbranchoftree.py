# 접근방법 : DFS로 트리를 순회하면 되겠구나! 
# 1. 기둥의 길이를 구하려면? 먼저 루트에서 출발해서 자식이 2개 이상이 되면 기가노드로 판정, 그때까지의 길이 누적합해서 기둥 길이 구하기
# 2. 가장 긴 가지의 길이를 구하려면? 앞에서 기둥 길이 구할 때 기가 노드를 찾아서 기가노드로부터 각 가지의 리프노드까지 DFS하기
# 근데 길이를 어떻게 더해줄지, weight를 어떻게 처리할지,,,, 디버깅이 굉장히 오래 걸림 ㅜㅜㅜ 
# 200000개다 보니 재귀로는 못 풀고, stack으로 어떻게 backtracking을 했었는지 기억이 안 나서 너무 힘들었던 문제였습니다

import sys
input = sys.stdin.readline

N, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(1, N):
    s,e,w = map(int, input().split())
    graph[s].append((e, w))  # 처음에는 그냥 한쪽으로 받아도 되지 않나? 했는데 계속 오류가 나서 이 부분은 gpt 도움 받았습니다
    graph[e].append((s, w))  # 양방향으로 받아야 한다고 하더라구요.. 아무래도 방향 그래프가 아니기 때문에...

visited = [0] * (N + 1)

# 기둥 길이 구하는 dfs(dfs도 아님)
def dfs_pillar(start):
    length = 0
    now = start
    visited[now] = 1

    while True:
        cnt = 0
        nxt_n = -1  # 다음 노드
        nxt_w = 0   # 다음 가중치

        for nxt, w in graph[now]:  #현재 갈 수 있는 노드 중
            if not visited[nxt]:   # 방문 안한 노드라면
                cnt += 1           # cnt 증가 (자식 노드 개수)
                nxt_n = nxt        # 다음 노드, 가중치 업데이트
                nxt_w = w
        if cnt != 1:              # 만약 기둥에 있는 노드라면 반복문 한번만 돌고 cnt가 1이 될 것
            return length, now    # 근데 1이 아니라는건 기가노드라는 뜻이기 때문에 함수 종료, 길이와 now(기가노드) return

        visited[nxt_n] = 1       # cnt가 1이라면 다음 노드 방문 처리, 기둥 길이 늘리기, now 업데이트
        length += nxt_w
        now = nxt_n

# 가장 긴 가지 길이 구하기
def dfs_branch(start):
    stack = [(start,0)]   # stack으로 DFS 구현, 시작점과 길이 넣어줌
    max_leng = 0          # 우리가 구하고 싶은 최대 길이를 가진 가지의 길이

    while stack:
        now, dist = stack.pop()    # stack에서 빼내기

        leaf = True                # 리프노드에 도달하면 멈춰야 하니까 일단 True로 초기화
        for nxt, weight in graph[now]:    # now에서 갈 수 있는 노드 탐색
            if not visited[nxt]:          # 아직 방문하지 않았다면 (DFS 시작하지 않은 길이라면)
                visited[nxt] = 1          # 방문 처리
                leaf = False              # 아직 갈 곳이 있다는 거니까 leaf 상태 False로 업데이트
                stack.append((nxt, dist+weight))        # 다음에 갈 곳이니까 stack에 추가, 거리도 튜플로 같이 업데이트
        if leaf:    # 리프노드에 도달하면
            max_leng = max(max_leng, dist)      # 최대 길이 업데이트
    return max_leng


length, giga = dfs_pillar(R)
print(length)
print(dfs_branch(giga))