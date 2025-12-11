import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

N = int(input())
num = [int(input()) for _ in range(N)]

result = 0
for _ in range(N-1):
  a = heappop(num)
  b = heappop(num)
  result += a+b
  heappush(num,a+b)

print(result)
