import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 유니온-파인드 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # 가중치가 맨 앞에 와야 정렬하기 편함
edges.sort()

# 부모 테이블
parent = [i for i in range(V + 1)]

total_weight = 0
edge_count = 0 # 간선 V-1개 모이면 종료해도 됨

# 간선 하나씩 확인하며 연결
for cost, a, b in edges:
    # 사이클이 발생하지 않는다면 (루트가 다르다면)
    if find(a) != find(b):
        union(a, b)
        total_weight += cost
        edge_count += 1
        if edge_count == V - 1: break # 최적화

print(total_weight)