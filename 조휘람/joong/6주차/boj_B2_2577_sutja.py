import sys
input = sys.stdin.readline
result = 1
for _ in range(3):
  result *= int(input())

dist = [0]*10
for i in str(result):
  dist[int(i)] += 1
for j in dist:
  print(j)