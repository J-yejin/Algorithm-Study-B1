import sys
sys.setrecursionlimit(10**6)

def find(node):
    if friends.get(node) is None:
        friends[node] = -1
        return node
    if type(friends.get(node)) == int and friends.get(node) < 0:
        return node
    friends[node] = find(friends[node])
    return friends[node]


def union(node_a, node_b):
    A = find(node_a)
    B = find(node_b)
    if A == B:
        return
    if A < B:
        friends[A] += friends[B]
        friends[B] = A
    else:
        friends[B] += friends[A]
        friends[A] = B
    return

T = int(input())
for _ in range(T):
    F = int(input())
    friends = {}
    for _ in range(F):
        name_a, name_b = sys.stdin.readline().split()
        union(name_a, name_b)
        print(-friends[find(name_a)])