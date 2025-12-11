import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [*map(int, input().split())]

def test(x):
  cnt = 1
  cur_min = arr[0]
  cur_max = arr[0]
  
  for v in arr[1:]:
    cur_min = min(cur_min, v)
    cur_max = max(cur_max, v)
    
    if cur_max - cur_min > x:
      cnt += 1
      cur_min = v
      cur_max = v
      if cnt > M:
        return False
  return True

min_result = 0
max_result = max(arr) - min(arr)
result = max_result 
while min_result <=max_result:
  mid = (min_result + max_result) // 2
  if test(mid):
    result = mid
    max_result = mid - 1
  else:
    min_result = mid + 1
print(result)

