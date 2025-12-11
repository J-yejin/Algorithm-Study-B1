import sys
input = sys.stdin.readline

N, C = map(int, input().split())

lst = [int(input()) for _ in range(N)]

lst.sort()


def test(mid):
    cnt = 1
    cur_g = lst[0]
    for i in range(1, N):
        if lst[i] - cur_g >= mid:
            cnt +=1
            cur_g = lst[i]
    if cnt >= C:
        return True
    else:
        return False

def bs():
    l = 1
    r = lst[-1] - lst[0]
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        
        if test(mid):
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
        
    return ans
print(bs())
    