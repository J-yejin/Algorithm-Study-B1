import sys


from heapq import heappop, heappush

arr = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n>=1:
        heappush(arr,-n)
    if n <0:
        continue
    if n == 0:
        if arr:
            print(-heappop(arr))
        else:
            print(n)
