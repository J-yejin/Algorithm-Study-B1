import sys
input = sys.stdin.readline
N, K = map(int, input().split())
number = [*map(int, input().split())]
temp = sum(number[:K])
result = temp
for i in range(K, N):
    temp += number[i]
    temp -= number[i-K]
    if temp > result:
      result = temp
print(result)
