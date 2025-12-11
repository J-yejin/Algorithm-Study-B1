N = int(input())
r = True
for i in range(1, N+1):
    s = i + sum([*map(int, str(i))])
    if s == N:
        r = False
        print(i)
        break
if r:
    print(0)