import sys
input = sys.stdin.readline
N = int(input())
N_lst = set(map(int, input().split()))
M = int(input())
M_lst = [*map(int, input().split())]
for i in M_lst:
  if i in N_lst:
    print(1)
  else:
    print(0)