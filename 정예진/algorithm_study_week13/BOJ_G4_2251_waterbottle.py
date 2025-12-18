# 접근 방법 : BFS인데.. 뭔가 어렵다.. 
# 뭔가 새로운 느낌의 BFS라 처음에 아이디어는 떠올렸는데 물 옮기는걸 어떻게 구현할지 그게 시간이 오래 걸렸음@
# point는 6가지 경우의 수를 따지는 것, visited로 한번 만들어진 상태는 다시 오지 않도록 하는 것
# 그리고 옮길 물의 양을 계산하는 방법 이거 3개를 떠올리는데 시간이 오래 걸렸다...

from collections import deque

A, B, C = map(int, input().split())

# 1. 초기 설정
res = []
visited = [[0] * 201 for _ in range(201)]
visited[0][0] = 1
capacity = [A, B, C]  # 입력 받은 물통 용량
q = deque([(0,0,C)])

# BFS
while q:
    a, b, c = q.popleft()
    if a == 0:
        res.append(c)

    # 현재 상태에 인덱스로 접근해 편하게 물 옮기려고 리스트로 만듦
    curr_state = [a, b, c]

    # 6가지 경우의 수 탐색 (보내는 곳 -> 받는 곳)
    # 0:A, 1:B, 2:C
    for sender in range(3):  # 보내는 물통
        for receiver in range(3):  # 받는 물통

            if sender == receiver:  # 같은 물통끼리는 못 옮기니까 패스
                continue

            # 다음 상태를 만들기 위해 현재 상태 복사
            next_state = curr_state[:]

            # 옮길 물의 양 계산
            # min(보내는 물통에 있는 양, 받는 물통의 남은 공간)  <- 이게 너무 어려웠음!
            amount = min(curr_state[sender], capacity[receiver] - curr_state[receiver])

            # 물 이동
            next_state[sender] -= amount
            next_state[receiver] += amount

            # visited는 A와 B의 양만으로 체크하면 C는 자동결정되니까 괜찮음
            if not visited[next_state[0]][next_state[1]]:
                visited[next_state[0]][next_state[1]] = 1
                q.append((next_state[0], next_state[1], next_state[2]))

print(*sorted(res))