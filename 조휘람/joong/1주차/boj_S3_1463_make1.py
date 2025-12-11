X = int(input())
result = 21e8
def recur(n, cnt):
    global result
    if n == 1:
        result = min(result, cnt)
        return
    if cnt >= result:
        return
    if not n%3:
        recur(n//3,cnt + 1)
    if not n%2:
        recur(n//2, cnt + 1)
    recur(n - 1, cnt + 1)
recur(X, 0)
print(result)
