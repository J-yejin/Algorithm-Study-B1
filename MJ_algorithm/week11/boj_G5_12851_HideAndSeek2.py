import sys
from collections import deque
import heapq

# input = sys.stdin.readline


sys.stdin = open('input.txt', 'r')

N, X = map(int, input().split())

visited = [0] *  100001

pq = []

heapq.heappush(pq, (0, N))

print(pq)

visited[N] = 1
min_time = 10**10
cur_time = 0

cnt = 0 #정답 갯수 저장

while pq:

    cur_time, cur_pos = heapq.heappop(pq)
    if cur_time > min_time :
        break  #다익스트라 가지치기
    
    if cur_pos == X : #도착했으면
        min_time = cur_time
        cnt += 1
        continue  
    
    for next_pos in [cur_pos-1, cur_pos+1, cur_pos *2] :
        if 0 > next_pos or next_pos > 100000 : #2차원 할 때랑 마찬가지로 좌표 조건검사
            continue
        
        if visited[next_pos] == 0 or visited[next_pos] == cur_time + 1 :
            visited[next_pos] = cur_time + 1
            heapq.heappush(pq, (cur_time+1, next_pos))


print(min_time)
print(cnt)
