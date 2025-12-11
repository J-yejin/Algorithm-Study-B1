import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
arr = [*map(int, input().split())]
arr = sorted(arr, reverse=False)
arr.append(L)
arr.insert(0,0)
# print(arr)
def test(x):
    cnt = 0
    for i in range(1, N+2):
        distance = arr[i] - arr[i - 1]
        cnt += (distance - 1) // x
    if cnt > M:
        return False
    else:
        return True


min_result = 1
max_result = max(arr)

while min_result <=max_result:
  mid = (min_result + max_result) // 2
  if test(mid):
    result = mid
    max_result = mid - 1
  else:
    min_result = mid + 1
print(result)