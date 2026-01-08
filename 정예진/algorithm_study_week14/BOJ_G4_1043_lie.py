# 접근 방법 : Union-Find / 같은 파티에 참여하면 트리로 묶어놓기, 진실을 아는 사람도 트리로 묶어놓기 -> 얘네의 노드는 0번(진실)
# 0번과 연결되어 있으면 진실을 아는 사람, 그리고 진실을 아는 사람이 있는 파티에 참여한 사람은 모두 루트가 0번으로 연결됨
# 0번과 연결된 사람이 있는 파티면 참여 X, 없으면 참여하도록 하면 지민이는 거짓말쟁이가 되지 않는다

import sys
input = sys.stdin.readline

# 유니온-파인드 함수 - MST랑 똑같은거 가져옴
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

N, M = map(int, input().split())

# 1. 사람 수만큼 부모 노드 초기화
parent = [i for i in range(N + 1)]

# 2. 진실을 아는 사람들을 0번과 묶기
truth_list = list(map(int, input().split()))[1:]  # 첫 번째 숫자는 사람 수라 제외
for person in truth_list:
    union(0, person)  # 0번과 하나의 트리로 묶음

# 3. 파티 참여하는 사람들끼리 트리로 연결
parties = []
for _ in range(M):
    party = list(map(int, input().split()))[1:]
    parties.append(party)

    # 파티에 온 사람들끼리만 묶어주면 됨 (첫 사람을 기준으로 싹 다 통합)
    for i in range(len(party) - 1):
        union(party[i], party[i + 1])

# 4. 각 파티별로 거짓말 가능한지 확인
ans = 0
for party in parties:
    # 파티원 중 아무나 한 명을 뽑아서 (party[0])
    # 그 사람의 대장이 0번(진실)인지 확인
    if find(party[0]) != find(0):
        ans += 1  # 0번과 연결 안 됐으면 거짓말 성공!

print(ans)
