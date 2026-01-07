import sys
input = sys.stdin.readline

V, E = map(int, input().split())

tree = [[*map(int, input().split())] for _ in range(E)]
