N,M = map(int,input().split())

People = [0]*(N+1)
Party = [0]*M

Q = []

for P in [*map(int,input().split())][1:]:
    People[P] = 1
    Q.append(P)

Party_Board = [[*map(int,input().split())][1:] for _ in range(M)]

while Q:
    person = Q.pop()
    for party_num in range(M):
        if Party[party_num] or person not in Party_Board[party_num]: continue
        Party[party_num] = 1
        for person_new in Party_Board[party_num]:
            if People[person_new]: continue
            People[person_new] = 1
            Q.append(person_new)

print(Party.count(0))