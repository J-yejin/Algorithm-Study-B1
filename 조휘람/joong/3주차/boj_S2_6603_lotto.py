import sys
input = sys.stdin.readline
def recur(n, p, result):
  global K, arr
  if n == 6:
    for i in result:
      print(i, end=' ')
    print()
  for i in range(p, K):
    result.append(arr[i])
    recur(n+1, i+1, result)
    result.pop()
    
while True:
  arr = [*map(int, input().split())]
  if not arr[0]:
    break
  K = arr.pop(0)
  arr.sort()
  recur(0, 0, [])
  print()