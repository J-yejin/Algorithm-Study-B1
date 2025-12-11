K, N = map(int, input().split())
a = [int(input()) for _ in range(K)]
def test(mid):
    cnt = 0
    result = False
    for i in range(K):
        cnt += a[i] // mid
    if cnt >= N:
        result = True
    return result


def bs():
    r = max(a)
    l = 1
    while l <= r:
        mid = (l + r) // 2

        if test(mid):
            l = mid + 1
        else:
            r = mid - 1
    return r

print(bs())