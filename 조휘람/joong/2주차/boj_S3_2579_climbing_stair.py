import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

dist = [0] * N

dist[0] = arr[0]
if N == 1:
    print(dist[0])
elif N == 2:
    dist[1] = arr[0] + arr[1]
    print(dist[1])
else:
    dist[1] = arr[0] + arr[1]
    for i in range(2,N):
        dist[i] = max((dist[i-3] + arr[i-1] + arr[i]), (dist[i-2] + arr[i]))
    print(dist[N-1])
