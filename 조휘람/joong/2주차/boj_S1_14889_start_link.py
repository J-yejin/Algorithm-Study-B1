import sys
input = sys.stdin.readline

N = int(input())

S = [[*map(int, input().split())] for _ in range(N)]
result = 21e8
def recur(n, p, s_lst):
    global result
    if n == N//2:
        l_lst = []
        for k in range(N):
            if k in s_lst:
                continue
            l_lst.append(k)
        cnt_s = 0
        cnt_l = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                cnt_s += S[s_lst[i]][s_lst[j]] + S[s_lst[j]][s_lst[i]]
                cnt_l += S[l_lst[i]][l_lst[j]] + S[l_lst[j]][l_lst[i]]
        result = min(abs(cnt_s - cnt_l), result)
        return
    for i in range(p,N):
        # append
        s_lst.append(i)
        recur(n+1, i+1, s_lst)
        s_lst.pop()
recur(0,0,[])
print(result)