N = int(input())
num = [i for i in range(1, N+1)]
used = [0] * N

def recur(n, lst):
   if n == N:
        print(*lst)
        return
   for i in range(N):
      if used[i]:
         continue
      used[i] = 1
      recur(n+1, lst+[num[i]])
      used[i] = 0
      
recur(0, [])