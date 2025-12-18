import sys
input = sys.stdin.readline

water = [*map(int, input().split())]
A, B, C = water

visited = [[0] * (B + 1) for _ in range(A + 1)]
results = []


def recur(a, b, c):
    visited[a][b] = 1
    if a == 0:
        results.append(c)
    cur_water = [a, b, c]
    for i in range(3):
        for j in range(3):
            if i == j: 
                continue
            
            move = min(cur_water[i], water[j] - cur_water[j])
            next_water = cur_water[:]
            next_water[i] -= move
            next_water[j] += move
            

            if not visited[next_water[0]][next_water[1]]:
                recur(next_water[0], next_water[1], next_water[2])


recur(0, 0, C)
results.sort()
print(*results)