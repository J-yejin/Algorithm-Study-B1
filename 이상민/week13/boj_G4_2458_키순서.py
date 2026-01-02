N,M = map(int,input().split())

Board_To = [[0]*N for _ in range(N)]
Board_From = [[0]*N for _ in range(N)]
Board_Root = [{i,} for i in range(N)]

for _ in range(M):
    start, end = map(int,input().split())
    Board_To[start-1][end-1] = 1
    Board_From[end-1][start-1] = 1

Q = []

for idx in range(N):
    if 1 in Board_From[idx]: continue
    Q.append(idx)

while Q:
    node = Q.pop()
    for node_next in range(N):
        if not Board_To[node][node_next]:continue
        Board_Root[node_next] |= Board_Root[node]
        Board_From[node_next][node] = 0
        if 1 in Board_From[node_next]:continue
        Q.append(node_next)

Res = 0

for node in range(N):
    flag = 1
    for node_other in range(N):
        if node_other in Board_Root[node]:continue
        if node in Board_Root[node_other]:continue
        flag = 0
        break

    Res += flag

print(Res)