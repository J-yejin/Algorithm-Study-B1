# 벨만 포드 : 음수 가중치가 있는 그래프에서 최단 경로를 찾는 알고리즘
# 전체 노드에 대해서 전체 간선 M개를 하나씩 다 확인
# -> (현재까지 아는 거리 + 이 간선의 비용) < 목적지의 기록된 거리면 갱신
# N개의 노드에서 최단 경로는 최대 N-1개의 간선을 거치니까 (N-1)번 반복
# https://wikidocs.net/206946 참고

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 노드 수, 간선 수
edges = []  # 모든 간선을 저장할 리스트
dist = [10e9] * (N + 1)  # 최단 거리 테이블

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

INF = 10e9

def bf(start):
    # 시작 노드 초기화
    dist[start] = 0

    # 전체 노드만큼 반복
    # N-1번은 최단 거리 갱신용, 마지막 1번은 음수 사이클 판별용
    for i in range(N):
        # 매 반복마다 모든 간선을 확인
        for cur_node, next_node, cost in edges:
            # 현재 노드를 거쳐서 가는 길이 더 빠르고, 현재 노드가 방문한 적 있는 곳이라면
            if dist[cur_node] != INF and dist[cur_node] + cost < dist[next_node]:
                dist[next_node] = dist[cur_node] + cost # 값 갱신

                # 만약 N번째 반복에서도 값이 갱신되면 음수 사이클 O
                if i == N - 1:
                    return True
    return False

cycle = bf(1)

if cycle:
    print("-1")
else:
    # 2번 노드부터 N번 노드까지 출력
    for i in range(2, N + 1):
        # 도달할 수 없는 경우 -1 출력
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])