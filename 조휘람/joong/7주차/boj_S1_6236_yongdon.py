import sys
input = sys.stdin.readline

N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)]

l = max(costs)
r = sum(costs)

def test(mid):
    cnt = 1
    money = mid
    for i in costs:
      if money < i:
        cnt += 1
        money = mid
      money -= i
    if cnt > M:
      result = False
    else:
      result = True
    return result


def bs():
    l = max(costs)
    r = sum(costs)
    ans = r
    while l <= r:
        mid = (l + r) // 2

        if test(mid):
           ans = mid
           r = mid - 1
        else:
            l = mid + 1
    return ans

print(bs())