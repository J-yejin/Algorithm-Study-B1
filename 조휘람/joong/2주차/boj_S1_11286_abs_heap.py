from heapq import heappush, heappop

N = int(input())
num = []
for _ in range(N):
    x = int(input())
    if not x:
        if not len(num):
            print(0)
            continue
        print(heappop(num)[1])
    else:
        heappush(num, (abs(x),x))
