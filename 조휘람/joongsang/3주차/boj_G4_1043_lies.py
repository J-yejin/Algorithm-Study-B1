import sys
input = sys.stdin.readline
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    
    if rank[a] < rank[b]:
        parents[a] = b
    elif rank[b] < rank[a]:
        parents[b] = a
    else:
        parents[b] = a
        rank[a] += 1
cnt = 0
#사람 수 N, 파티 수 M
N, M = map(int, input().split())
#이야기 진실을 아는 사람의 수 K
k_num = [*map(int, input().split())]
K = k_num[0]
truth = k_num[1:]
graph = []
parents = [i for i in range(N + 1)]
rank = [0] * (N + 1)
for _ in range(M):
    pp_lst = [*map(int, input().split())]
    pp_num = pp_lst.pop(0)
    graph.append(((pp_lst)))
    
    if pp_num >= 2:
        f = pp_lst[0]
        for p in pp_lst[1:]:
            union(f, p)


if not K:
    print(M)
else:        
    truth_parents = set(find(x) for x in truth)
        
    for party in graph:
        lie = True
        for person in party:
            if find(person) in truth_parents:
                lie = False
                break
        if lie:    
            cnt += 1
    print(cnt)
            
    