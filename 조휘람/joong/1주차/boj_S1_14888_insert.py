import sys
input = sys.stdin.readline

N = int(input())
num = [*map(int,input().split())]
operator = [*map(int,input().split())]
cnt = num[0]
max_result = -21e8
min_result = 21e8



def recur(n, k, cnt, pl, mi, mul, div):
    global max_result, min_result
    if n == N:
        max_result = max(cnt, max_result)
        min_result = min(cnt, min_result)
        return
    for i in range(k,N):
        if pl:
            recur(n+1,i+1, cnt+num[i], pl-1, mi, mul, div)
        if mi:
            recur(n + 1, i + 1, cnt - num[i], pl, mi - 1, mul, div)
        if mul:
            recur(n + 1, i + 1, cnt * num[i], pl, mi, mul - 1, div)
        if div:
            recur(n + 1, i + 1, int(cnt / num[i]), pl, mi, mul, div - 1)

recur(1, 1, cnt, operator[0], operator[1], operator[2], operator[3])
print(max_result)
print(min_result)