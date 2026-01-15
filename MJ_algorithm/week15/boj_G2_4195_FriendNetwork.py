import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T+1):

    def find(x):
        if x not in parent:
            parent[x] = x
            number[x] = 1
            return x
        
        if parent[x] == x:
            return x
        
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)

        if rootX != rootY:
            parent[rootY] = rootX
            number[rootX] += number[rootY]

        print(number[rootX])

    N  = int(input())
    
    parent = {}
    number = {}

    for _ in range(N):
        f1, f2 = input().split()
        union(f1, f2)

        