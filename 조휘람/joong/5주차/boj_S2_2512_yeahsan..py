N = int(input())
li = [*map(int, input().split())]
wh = int(input())

def test(mid):
  result = True
  cnt = 0
  if mid * N > wh:
    result = False
    return False
  for i in li:
    if i > mid:
      cnt += mid
    else:
      cnt += i
  if cnt > wh:
    result = False
    
  return result

def bs():
  r = wh
  l = 1
  mid = (l + r) // 2
  while l <= r:
    if test(mid):
      l = mid + 1
    else:
      r = mid - 1
  return r

print(bs())
      
  
                     