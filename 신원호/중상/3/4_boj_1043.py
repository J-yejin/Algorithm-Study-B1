# boj 1043 거짓말
# union-find

import sys

def find(a):
    # 경로 압축
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return


N, M = map(int, input().split())
parent = list(range(N + 1))
# parent[i] == 0: i는 진실을 알고 있음
num_of_truth, *truth = list(map(int, sys.stdin.readline().split()))
for i in truth:
    union(0, i)
parties = []
for _ in range(M):
    num_of_attendance, *party = list(map(int, sys.stdin.readline().split()))
    parties.append(party)
    for j in range(num_of_attendance - 1):
        union(party[j], party[j + 1])
result = 0
# 한 파티에 참여한 인원들끼리는 진실을 알고있음의 여부가 같아야함
for party in parties:
    if find(party[0]) != 0:
        result += 1
print(result)