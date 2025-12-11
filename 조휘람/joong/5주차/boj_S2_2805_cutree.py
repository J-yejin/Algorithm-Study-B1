N, M = map(int, input().split())
tree = [*map(int, input().split())]

def test(mid):
    cnt = 0
    result = False
    for i in range(N):
      if tree[i] - mid <= 0:
        continue
      cnt += tree[i] - mid
    if cnt >= M:
      result = True
    return result


def bs():
    r = max(tree)
    l = 1
    while l <= r:
      mid = (l + r) // 2

      if test(mid):
        l = mid + 1
      else:
        r = mid - 1
    return r
print(bs())